<<<<<<< HEAD
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from htmlTemplates import css, bot_template, user_template
import google.generativeai as genai
import pickle
import os

# Load environment variables
load_dotenv()

# Configure Google Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Extract text from uploaded PDF documents
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Split text into smaller chunks for processing
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=50000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

# Create FAISS vector store
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

# Set up the conversational chain for answering questions
def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context. If the answer is not in
    the provided context, just say, "The answer is not available in the context." Do not provide incorrect information.
    
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

# Load FAISS index with error handling
def load_faiss_index_with_debugging(index_path, embeddings):
    try:
        vector_store = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
        return vector_store
    except pickle.UnpicklingError:
        st.error("Unpickling error occurred! The FAISS index file might be corrupted.")
    except Exception as e:
        st.error(f"Error loading FAISS index: {e}")

# Handle user input
def handle_user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = load_faiss_index_with_debugging("faiss_index", embeddings)

    if vector_store:
        docs = vector_store.similarity_search(user_question)
        chain = get_conversational_chain()
        response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
        st.session_state.chat_history.append({"user": user_question, "bot": response["output_text"]})

# Main app function
def main():
    st.set_page_config(page_title="Multi-PDF Chatbot", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    # Initialize chat history in session state if not already done
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "faiss_index" not in st.session_state:
        st.session_state.faiss_index = False  # Track if the index has been built

    st.header("Multi-PDF Chatbot :books:")

    # Sidebar for uploading PDFs
    with st.sidebar:
        st.subheader("Upload your PDF documents")
        pdf_docs = st.file_uploader("Upload PDFs", accept_multiple_files=True)
        if st.button("Process"):
            if pdf_docs:
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    get_vector_store(text_chunks)
                    st.session_state.faiss_index = True  # Set index built status
                    st.success("Processing complete!")
            else:
                st.error("Please upload at least one PDF file.")

    # Check if a file has been uploaded and processed
    if st.session_state.faiss_index:
        # User input for questions
        user_question = st.text_input("Ask a question about the PDFs:")
        if user_question:
            handle_user_input(user_question)
    else:
        user_question = st.text_input("Ask a question about the PDFs:")
        if user_question:
            st.write("Please upload and process PDF files before asking questions.")

     # Display chat history
    
    for chat in st.session_state.chat_history:
        st.write(user_template.replace("{{MSG}}", chat["user"]), unsafe_allow_html=True)
        st.write(bot_template.replace("{{MSG}}", chat["bot"]), unsafe_allow_html=True)
        
if __name__ == "__main__":
    main()
=======
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from htmlTemplates import css, bot_template, user_template
import google.generativeai as genai
import pickle
import os

# Load environment variables
load_dotenv()

# Configure Google Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Extract text from uploaded PDF documents
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Split text into smaller chunks for processing
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=50000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

# Create FAISS vector store
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

# Set up the conversational chain for answering questions
def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context. If the answer is not in
    the provided context, just say, "The answer is not available in the context." Do not provide incorrect information.
    
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

# Load FAISS index with error handling
def load_faiss_index_with_debugging(index_path, embeddings):
    try:
        vector_store = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
        return vector_store
    except pickle.UnpicklingError:
        st.error("Unpickling error occurred! The FAISS index file might be corrupted.")
    except Exception as e:
        st.error(f"Error loading FAISS index: {e}")

# Handle user input
def handle_user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = load_faiss_index_with_debugging("faiss_index", embeddings)

    if vector_store:
        docs = vector_store.similarity_search(user_question)
        chain = get_conversational_chain()
        response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
        st.session_state.chat_history.append({"user": user_question, "bot": response["output_text"]})

# Main app function
def main():
    st.set_page_config(page_title="Multi-PDF Chatbot", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "faiss_index" not in st.session_state:
        st.session_state.faiss_index = False  # Track if the index has been built

    st.header("Multi-PDF Chatbot :books:")

    # Sidebar for uploading PDFs
    with st.sidebar:
        st.subheader("Upload your PDF documents")
        pdf_docs = st.file_uploader("Upload PDFs", accept_multiple_files=True)
        if st.button("Process"):
            if pdf_docs:
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    get_vector_store(text_chunks)
                    st.session_state.faiss_index = True  # Set index built status
                    st.success("Processing complete!")
            else:
                st.error("Please upload at least one PDF file.")

    # Check if a file has been uploaded and processed
    if st.session_state.faiss_index:
        # User input for questions
        user_question = st.text_input("Ask a question about the PDFs:")
        if user_question:
            handle_user_input(user_question)
    else:
        user_question = st.text_input("Ask a question about the PDFs:")
        if user_question:
            st.write("Please upload and process PDF files before asking questions.")

    # Display chat history
    
    for chat in st.session_state.chat_history:
        st.write(user_template.replace("{{MSG}}", chat["user"]), unsafe_allow_html=True)
        st.write(bot_template.replace("{{MSG}}", chat["bot"]), unsafe_allow_html=True)
    

if __name__ == "__main__":
    main()
>>>>>>> 7f47261 (initial commit)
