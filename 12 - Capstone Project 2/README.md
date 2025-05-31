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

Ask questions about Linux manuals and documentation. This chatbot retrieves answers from uploaded PDF manuals and provides references to the document and page number.

## 🚀 How to Use

1. Type a Linux-related question into the input box.
2. The chatbot will respond using the document content.
3. Citations will include the file name and page number.

## 🧠 Powered by

- LangChain
- OpenAI (GPT-4)
- FAISS
- PDF parsing with PyMuPDF
- Streamlit

## 📂 Data Source

Documents stored in `data/` are indexed for retrieval. All `.pdf` files are handled via Git LFS.

## 🔐 Note

This Space uses Git LFS for binary PDF files.