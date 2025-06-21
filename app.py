import os
import uuid
from dotenv import load_dotenv
from flask import Flask, request, render_template, session, jsonify
from flask_session import Session

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load .env variables
load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Chat initialization
def initialize_chatbot():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("user", "Question: {question}")
    ])
    llm = Ollama(model="llama3")
    output_parser = StrOutputParser()
    return prompt | llm | output_parser

chain = initialize_chatbot()

@app.route('/')
def index():
    session["chat_id"] = str(uuid.uuid4())  # New session each time
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    chat_id = session.get("chat_id")
    if not chat_id:
        return jsonify({"error": "Session not found"}), 400

    key = f"chat_history_{chat_id}"
    data = request.json or {}
    question = data.get("question", "").strip()

    if key not in session:
        session[key] = []

    if not question:
        return jsonify({"answer": "", "history": session[key]})

    answer = chain.invoke({"question": question})

    session[key].append({"role": "user", "text": question})
    session[key].append({"role": "assistant", "text": answer})
    session.modified = True

    return jsonify({"answer": answer, "history": session[key]})

if __name__ == '__main__':
    app.run(debug=True)
