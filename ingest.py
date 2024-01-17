from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

DATA_PATH = "data/"
DB_FAISS_PATH = "vectorstore/db_faiss"


# Create vector database
def create_vector_db():
    print("1")
    loader = DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
    print("2")
    documents = loader.load()
    print("3")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    print("4")
    texts = text_splitter.split_documents(documents)
    print("5")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
    )
    print("6")
    db = FAISS.from_documents(texts, embeddings)
    print("7")
    db.save_local(DB_FAISS_PATH)
    print("8")


if __name__ == "__main__":
    create_vector_db()
