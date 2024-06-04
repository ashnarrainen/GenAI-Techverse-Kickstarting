from qdrant_client import QdrantClient
from llama_index import VectorStoreIndex, ServiceContext, SimpleDirectoryReader
from llama_index.llms import Ollama
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore


llm = Ollama(model="mistral", request_timeout=360)

prompt = "Hi in a few words"

response = llm.complete(prompt, True)
print(response)
