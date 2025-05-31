---
title: "Linux Documentation Support Chatbot"
emoji: 📘
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: 1.32.0
app_file: app.py
pinned: false
license: mit
---

# 📘 Linux Documentation Support Chatbot

The Linux Documentation Support Chatbot is a Retrieval-Augmented Generation (RAG) application built with Python and Streamlit. It serves as a customer support assistant for Linux-related questions by:

* Ingesting multiple Linux documentation sources (PDFs and text files).
* Indexing content with OpenAI embeddings and a vector database (Chroma/FAISS).
* Providing a conversational chat interface that cites document names and page numbers for each answer.
* Offering GitHub Issue creation for questions that cannot be answered from the docs.

## 🚀 How to Use

1. Type a Linux-related question into the input box.
2. The chatbot will respond using the document content.
3. Citations will include the file name and page number.

## 📂 Repository Structure

```
linux-support-bot/
├── data/                      # Documentation storage
│   ├── The_Linux_Users_Guide.pdf
│   ├── grd1-en-manual.pdf 
│   └── lfpub_enterprise_os_practical_introduction_080818.pdf
├── app.py                     # Streamlit application entrypoint
├── doc_loader.py              # Document loading, splitting, and vector store creation
├── qa_system.py               # LangChain conversational retrieval chain with citation prompts
├── ticket_system.py           # GitHub Issue submission utility
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## 🧠 Powered by

- LangChain
- OpenAI (GPT-4)
- FAISS
- PDF parsing with PyMuPDF
- Streamlit

---

## 🔧 Prerequisites

* Python 3.9 or newer
* An OpenAI API key with access to embeddings and chat models
* A GitHub personal access token with `repo` scope

---

## ⚙️ Environment Variables

Before running or deploying the app, set the following environment variables:

| Name             | Description                                                    |
| ---------------- | -------------------------------------------------------------- |
| `OPENAI_API_KEY` | Your OpenAI API key                                            |
| `GITHUB_TOKEN`   | GitHub personal access token with repository issue permissions |
| `GITHUB_REPO`    | Target repository for issues in the form `owner/repo`          |

On Hugging Face Spaces, add these under **Settings & Secrets**.

---

## ☁️ Hugging Face Space

Follow this link: https://huggingface.co/spaces/RustSa/linux_documentation_support_chatbot
---
