from fastapi import FastAPI
from pydantic import BaseModel

from langchain_google_genai import ChatGoogleGenerativeAI , GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")


app=FastAPI(
    title="PDF RAG Chatbot API",
    description="Backend API for PDF question answering using RAG",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message":"PDF RAG Chatbot API is running!"}


class QuestionRequest(BaseModel):
    question:str

@app.post("/ask")
def user_question(request:QuestionRequest):

    response=retrieval.invoke({
        "input":request.question
    })
    return{
        "question":request.question,
        "answer":response["answer"]
    }


loader=PyPDFLoader("Data_Science Notes.pdf")
document=loader.load()
print(f"Loaded {len(document)} documents")

text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
    )

chunks=text_splitter.split_documents(document)
print(f"Split into {len(chunks)} chunks")

embeddings=GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=api_key
)

vector_stores=FAISS.from_documents(chunks,embeddings)

retriever=vector_stores.as_retriever(search_kwargs={"k":3})

llm=ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    google_api_key=api_key,
    temperature=0
)

prompt=ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Answer the user's question only using the provided context.

If the answer is not available in the context,
say "I couldn't find the answer in the uploaded PDF."

Context:
{context}

Question:
{input}
""")

document_chain=create_stuff_documents_chain(
    llm,prompt
)

retrieval=create_retrieval_chain(
    retriever,
    document_chain
)