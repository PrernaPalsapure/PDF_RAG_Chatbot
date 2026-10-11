# 📄 PDF RAG Chatbot using Gemini, LangChain & FAISS

A **Retrieval-Augmented Generation (RAG) based PDF Question Answering System** built using Python, Google Gemini, LangChain, FAISS, Streamlit, and FastAPI.

This project allows users to ask questions about PDF documents. It retrieves relevant text chunks using semantic similarity search and generates context-aware answers using Google's Gemini language model.

The project includes a Streamlit application, a separate FastAPI backend, and a Jupyter Notebook for exploring the RAG workflow.

## 🚀 Features

- 📄 Load and process PDF documents
- ✂️ Split extracted text into overlapping chunks
- 🔢 Generate vector embeddings using Google Gemini Embeddings
- 🗄️ Store and search embeddings using FAISS
- 🔍 Retrieve relevant document chunks through semantic search
- 🤖 Generate context-aware answers using Gemini Flash
- 🖥️ Interactive PDF question-answering interface using Streamlit
- ⚡ REST API for question answering using FastAPI
- 📝 Request validation using Pydantic
- 🔐 Load API credentials securely through environment variables
- 📓 Jupyter Notebook for exploring the RAG pipeline

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web interface for PDF question answering |
| FastAPI | REST API backend |
| Pydantic | Request data validation |
| LangChain | RAG pipeline and LLM integration |
| Google Gemini API | Language model and embeddings |
| FAISS | Vector storage and similarity search |
| PyPDFLoader | PDF text extraction |
| RecursiveCharacterTextSplitter | Text chunking |
| Jupyter Notebook | Experimentation and workflow exploration |

## 🏗️ Project Architecture

The project contains two Python applications that currently run independently.

### 1. Streamlit Application — `app.py`

The Streamlit application provides the user interface and runs the RAG workflow directly.

Workflow:

1. Upload a PDF document.
2. Extract text using PyPDFLoader.
3. Split the text into overlapping chunks.
4. Generate embeddings using Google Gemini.
5. Store the embeddings in FAISS.
6. Retrieve relevant chunks for the user's question.
7. Generate and display an answer using Gemini Flash.

### 2. FastAPI Backend — `api.py`

The FastAPI application exposes REST endpoints for health checking and question answering.

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check whether the API is running |
| POST | `/ask` | Submit a question and receive an answer |

The `/ask` endpoint accepts a JSON request:

```json
{
  "question": "What is machine learning?"
}
```

Example response:

```json
{
  "question": "What is machine learning?",
  "answer": "Machine learning is..."
}
```

**Note:** The current FastAPI implementation loads `Data_Science Notes.pdf` when the application starts. The PDF must be available at the configured path. The Streamlit application separately processes the PDF uploaded by the user.

The Streamlit application does not currently send requests to the FastAPI backend; they are separate implementations of the question-answering workflow.

## 🔄 RAG Workflow

```text
PDF Document
     |
     v
PyPDFLoader
     |
     v
Text Extraction
     |
     v
Text Chunking
     |
     v
Gemini Embeddings
     |
     v
FAISS Vector Store
     |
     v
Semantic Retrieval
     |
     v
Relevant Context + Question
     |
     v
Gemini Flash
     |
     v
Generated Answer
```

## ⚙️ How It Works

### Step 1 — PDF Loading

PyPDFLoader extracts text from the PDF and preserves document metadata, such as page information.

### Step 2 — Text Chunking

RecursiveCharacterTextSplitter divides the extracted text into smaller, overlapping chunks.

- Chunk size: 1000 characters
- Chunk overlap: 200 characters

Overlapping chunks help preserve context across chunk boundaries.

### Step 3 — Embedding Generation

GoogleGenerativeAIEmbeddings converts text chunks into numerical vectors that represent their semantic meaning.

### Step 4 — Vector Storage

FAISS stores the embeddings and supports efficient similarity searches to identify relevant document chunks.

### Step 5 — Context Retrieval

When a user asks a question, the retriever searches for semantically relevant chunks.

- Streamlit application: retrieves up to 4 chunks.
- FastAPI application: retrieves up to 3 chunks.

### Step 6 — Answer Generation

The retrieved context and question are passed to Gemini Flash. The prompt instructs the model to answer using the provided context and indicate when the answer cannot be found in the PDF.

## 💻 Getting Started

### Prerequisites

- Python 3.10 or a compatible version for the installed dependencies
- A Google Gemini API key
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/PrernaPalsapure/PDF_RAG_Chatbot.git
cd PDF_RAG_Chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Install the packages used by the project:

```bash
pip install streamlit fastapi "uvicorn[standard]" python-dotenv pydantic langchain langchain-community langchain-google-genai langchain-text-splitters faiss-cpu pypdf
```

### 4. Configure Your API Key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

Replace the placeholder with your own API key.

**Security:** Never commit your `.env` file or expose your API key in source code.

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, upload a PDF, and start asking questions.

### 6. Run the FastAPI Backend

Ensure `Data_Science Notes.pdf` is present at the path expected by `api.py`, then run:

```bash
uvicorn api:app --reload
```

Open the interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

Use the `POST /ask` endpoint to submit questions.

### 7. Explore the Notebook

Open `PDF_RAG_Chatbot.ipynb` in Jupyter Notebook or Google Colab to explore the RAG workflow interactively.

## 📁 Project Structure

```text
PDF_RAG_Chatbot/
│
├── app.py                  # Streamlit application
├── api.py                  # FastAPI backend
├── PDF_RAG_Chatbot.ipynb   # Jupyter Notebook
├── README.md               # Project documentation
├── .env                    # Local API credentials (not committed)
├── .gitignore              # Files excluded from Git
└── Data_Science Notes.pdf  # Required by the current FastAPI implementation
```

The PDF and environment files should only be included in the repository if appropriate. Do not commit private documents or credentials.

## 📚 Key Concepts

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- Large Language Models (LLMs)
- Prompt Engineering
- Vector Databases
- REST API Development
- Request Validation
- Document Processing
- LLM Application Development

## 🔮 Future Improvements

- Connect the Streamlit frontend to the FastAPI backend.
- Add support for multiple PDF uploads and document selection.
- Avoid rebuilding embeddings for every question.
- Add conversation history and follow-up question support.
- Display source page references for generated answers.
- Add automated tests and improved error handling.
- Deploy the application for public access.

## 👩‍💻 Author

**Prerna Palsapure**

AI/ML Engineer | Python | Machine Learning | Generative AI | LLMs | RAG Applications
## ⭐ If you found this project useful, consider giving it a star!
