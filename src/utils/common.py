# This file will contain common functions that are used in multiple places in the codebase

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings


# Function to extract data from the pdf file
def extract_data_from_pdf(data_dir):
    """
    Function to extract data from the pdf file
    
    Args:
    data_dir : str : Path to the directory containing the pdf files
    
    Returns:
    documents : list : List of documents extracted from the pdf files
    """
    
    loader = DirectoryLoader(data_dir, glob = "*.pdf", loader_cls = PyPDFLoader)
    documents = loader.load()
    return documents

# Function to split the text into chunks
def split_text_into_chunks(documents):
    """
    Function to split the text into chunks
    
    Args:
    documents : list : List of documents
    
    Returns:
    chunks : list : List of chunks with text split into chunks
    """
    
    splitter = RecursiveCharacterTextSplitter(chunk_size = 1500, chunk_overlap = 20)
    chunks = splitter.split_documents(documents)
    return chunks

# Function to download the embedding model
def download_embedding_model():
    """
    Function to download the embedding model
    
    Args:
    model_name : str : Name of the model to download
    
    Returns:
    embeddings : object : Embedding model object
    """
    
    embeddings = SentenceTransformerEmbeddings(model_name="NeuML/pubmedbert-base-embeddings")
    return embeddings