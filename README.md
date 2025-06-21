# 🤖 LLaMA 3 Chatbot – Flask App with LangChain & Ollama

A lightweight, open-source chatbot powered by **LLaMA 3** using **Ollama**, built with **Flask** and **LangChain**.  
This project provides a web interface similar to ChatGPT — but fully local, with no login required.

---

## 🚀 Features

- 💬 Conversational chatbot using LLaMA 3 (via Ollama)
- 🧠 LangChain integration for prompt formatting and chaining
- 🌐 Flask web app with clean ChatGPT-style UI
- 📂 Session-based chat history (new session on every page load)
- 🔓 No login or cloud dependency (runs entirely on your machine)

---

## 📸 UI Preview

> Sidebar with chat history + right side conversation window  
> Simple, clean, responsive UI (like ChatGPT)

---

## 🔧 Tech Stack

- Python 🐍
- Flask
- LangChain
- Ollama (for LLaMA 3 model)
- HTML/CSS (ChatGPT-style layout)

---

## 📥 Installation

### 1. Install [Ollama](https://ollama.com/)
```bash
ollama serve
ollama pull llama3
