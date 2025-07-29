from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()
embedding = HuggingFaceEndpointEmbeddings(repo_id='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]
res = embedding.embed_query(documents[0])
print(res)

vector = embedding.embed_documents(documents)
print(str(vector))