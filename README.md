# 📄 PDF RAG Chatbot using Gemini, LangChain & FAISS

A Retrieval-Augmented Generation (RAG) based PDF Question Answering system built using **Google Gemini**, **LangChain**, and **FAISS**.

The application allows users to ask questions about the contents of a PDF document by retrieving the most relevant text chunks using semantic search and generating context-aware responses using Gemini.

---

## 🚀 Features

- 📄 Load PDF documents
- ✂️ Split text into overlapping chunks
- 🔢 Generate vector embeddings using Gemini Embeddings
- 🗄️ Store embeddings in FAISS Vector Database
- 🔍 Perform semantic similarity search
- 🤖 Generate accurate answers using Gemini LLM
- ⚡ Built using LangChain Retrieval-Augmented Generation (RAG) pipeline

---

## 🛠️ Technologies Used

- Python
- Google Gemini API
- LangChain
- FAISS
- PyPDFLoader
- RecursiveCharacterTextSplitter
- GoogleGenerativeAIEmbeddings
- ChatGoogleGenerativeAI

---

## 📂 Project Workflow

```
PDF
   │
   ▼
PyPDFLoader
   │
   ▼
Extract Text
   │
   ▼
Text Splitter
   │
   ▼
Gemini Embeddings
   │
   ▼
FAISS Vector Database
   │
   ▼
Retriever
   │
   ▼
Prompt Template
   │
   ▼
Gemini LLM
   │
   ▼
Generated Answer
```

---

## 📌 How It Works

### Step 1 — Load PDF

The PDF document is loaded using **PyPDFLoader**, which extracts the text along with page metadata.

---

### Step 2 — Split the Text

The extracted text is divided into smaller overlapping chunks using **RecursiveCharacterTextSplitter**.

This improves retrieval accuracy while preserving context.

Example:

- Chunk Size = 1000
- Chunk Overlap = 200

---

### Step 3 — Create Embeddings

Each chunk is converted into high-dimensional vector embeddings using

**GoogleGenerativeAIEmbeddings**

Embeddings capture the semantic meaning of the text rather than exact words.

---

### Step 4 — Store Embeddings

All embeddings are stored inside a **FAISS Vector Database**.

FAISS enables fast similarity search even for thousands of document chunks.

---

### Step 5 — Retrieve Relevant Chunks

When the user asks a question,

- the question is converted into an embedding
- the Retriever searches FAISS
- the most relevant chunks are returned

Only these retrieved chunks are sent to the LLM.

---

### Step 6 — Generate Response

The retrieved context along with the user's question is passed to **Gemini Flash**, which generates the final answer.

---

## 📸 Sample Query

**Question**

```
What is this PDF about?
```

**Output**

```
The PDF discusses...
```

---

## 📁 Project Structure

```
PDF_RAG_Chatbot/
│
├── PDF_RAG_Chatbot_Gemini_FAISS_LangChain.ipynb
├── README.md
└── Data_Science Notes.pdf
```

---

## 📈 Future Improvements

- Streamlit Web Interface
- Multiple PDF Upload Support
- Chat History
- Conversation Memory
- Source Page References
- Deployment using Streamlit Cloud

---

## 📚 Concepts Used

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- Large Language Models (LLMs)
- Prompt Engineering
- FAISS Vector Database
- LangChain Pipelines

---

## 👩‍💻 Author

**Prerna Palsapure**

Aspiring Data Analyst | Machine Learning Enthusiast | Learning Generative AI & LLM Applications

---

## ⭐ If you found this project useful, consider giving it a star!
