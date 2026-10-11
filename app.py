import os
import asyncio
import streamlit as st

# Fix event-loop issue with Streamlit + gRPC/Gemini
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from dotenv import load_dotenv
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS


# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not found in .env file.")
    st.stop()

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


# Page configuration
st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="📄"
)

st.title("📄 PDF RAG Chatbot")
st.write("Ask questions from your PDF using Retrieval-Augmented Generation.")


# Upload PDF
uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)


if uploaded_file is not None:

    # Save uploaded PDF temporarily
    pdf_path = "uploaded_document.pdf"

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())


    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()


    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    st.success(f"PDF loaded successfully! Created {len(chunks)} text chunks.")


    # Create embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )


    # Create FAISS vector database
    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )


    # Create retriever
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )


    # Create Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        temperature=0.2
    )


    # Question input
    question = st.text_input(
        "Ask a question about your PDF:"
    )


    if question:

        # Retrieve relevant documents
        relevant_docs = retriever.invoke(question)


        # Combine retrieved context
        context = "\n\n".join(
            [doc.page_content for doc in relevant_docs]
        )


        # Prompt
        prompt = f"""
You are a helpful PDF question-answering assistant.

Answer the question using ONLY the information provided
in the context below.

If the answer is not available in the context,
say: "I could not find the answer in the uploaded PDF."

Context:
{context}

Question:
{question}

Answer:
"""


        # Generate answer
        response = llm.invoke(prompt)


        st.subheader("Answer")
        st.write(response.content)