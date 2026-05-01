from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def process_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    print("Documents:", len(documents))  # 👈 check

    splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(documents)

    print("Chunks:", len(chunks))  # 👈 check

    embeddings = OpenAIEmbeddings()

    if not chunks:
        raise ValueError("No chunks created from PDF")

    vector_store = FAISS.from_documents(chunks, embeddings)

    return vector_store

def get_answer(vector_store, query):
    docs = vector_store.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    return context