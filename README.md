# 📄 Chat with PDF (RAG Application)

An AI-powered application that allows users to **upload a PDF and ask questions**, with answers generated strictly from the document content using **Retrieval-Augmented Generation (RAG)**.

This project demonstrates how to combine **embeddings, vector databases (FAISS), and LLMs** to build context-aware AI systems.

---

## 🚀 Demo

*(Add your deployed app link here — Streamlit Cloud / AWS / Render)*
https://chat-with-pdf-suraj.streamlit.app/
---

## 📌 Features

* 📤 Upload a PDF document
* 💬 Ask questions in natural language
* 🔍 Retrieves relevant content from the PDF
* 🤖 Generates accurate, context-based answers
* ⚡ Real-time response generation
* 🧠 Reduces hallucination using RAG

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (UI)
* **LangChain** (RAG pipeline)
* **FAISS** (vector database)
* **OpenAI API** (LLM + embeddings)
* **PyPDF** (PDF parsing)

---

## 🧱 Project Structure

```id="d85c2v"
chat-pdf/
│
├── app.py              # Streamlit UI
├── rag.py              # PDF processing + retrieval logic
├── llm.py              # LLM response generation
├── .env                # API key (not committed)
├── requirements.txt    # Dependencies
├── README.md           # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash id="vxu9dz"
git clone https://github.com/your-username/chat-pdf.git
cd chat-pdf
```

### 2️⃣ Create virtual environment

```bash id="p5cxqi"
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash id="qg3ns1"
pip install -r requirements.txt
```

### 4️⃣ Add API Key

Create a `.env` file:

```id="6r1h9c"
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash id="yd3frd"
streamlit run app.py
```

---

## 🧠 How It Works (RAG Pipeline)

```id="5r5q4s"
PDF → Text Extraction → Chunking → Embeddings → FAISS Index
                                      ↓
                             User Query → Similarity Search
                                      ↓
                          Relevant Context → LLM → Answer
```

### Step-by-step:

1. Upload PDF
2. Extract text using PyPDFLoader
3. Split text into chunks
4. Convert chunks into embeddings
5. Store embeddings in FAISS
6. User asks a question
7. Retrieve top relevant chunks
8. Send context + question to LLM
9. Generate final answer

---

## 🎯 Learning Outcomes

* Understanding **RAG (Retrieval-Augmented Generation)**
* Working with **embeddings and vector databases**
* Implementing **semantic search using FAISS**
* Reducing LLM hallucinations using context grounding
* Building end-to-end AI applications

---

## 🔍 Key Concepts

### Embeddings

Convert text into numerical vectors to measure similarity.

### FAISS

Efficient vector search engine to retrieve relevant content.

### RAG

Combines retrieval + generation to produce accurate answers.

---

## 📊 Example Use Cases

* Document Q&A systems
* Research paper analysis
* Resume screening tools
* Knowledge base assistants
* Legal/financial document querying

---

## ⚡ Future Improvements

* 💬 Chat history (multi-turn conversation)
* 📚 Show source references (important for trust)
* 📄 Multi-PDF support
* 🔎 Hybrid search (keyword + vector)
* 🌐 Deployment with authentication

---

## 📸 Screenshots

*(Add UI screenshots here)*
<img width="327" height="357" alt="image" src="https://github.com/user-attachments/assets/7d0dfcaf-b8c1-4aa6-a660-11d05ed12ba7" />

---

## 🤝 Contributing

Contributions are welcome! Fork the repo and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 💡 Author

**Suraj Satav**
Generative AI Engineer 🚀
