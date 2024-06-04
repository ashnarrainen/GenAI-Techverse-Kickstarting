from qdrant_client import QdrantClient
from llama_index import VectorStoreIndex, ServiceContext, SimpleDirectoryReader
from llama_index.llms import Ollama
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore


def load_documents():
    return SimpleDirectoryReader("./data").load_data(True)


def create_qdrant_client():
    return QdrantClient(path="./qdrant_data")


def create_vector_store(client):
    return QdrantVectorStore("TrainedData", client=client)


def create_storage_context(vector_store):
    return StorageContext.from_defaults(vector_store=vector_store)


def create_llama():
    return Ollama(model="mistral", request_timeout=300.0)


def create_service_context(llm):
    return ServiceContext.from_defaults(llm=llm, embed_model="local")


def create_index(documents, service_context, storage_context):
    return VectorStoreIndex.from_documents(
        documents, service_context=service_context, storage_context=storage_context
    )


def create_query_engine(index):
    return index.as_query_engine(streaming=True, similarity_top_k=1)


def query_data(query_engine, query):
    return query_engine.query(query)


def print_response_stream(response_stream):
    response_stream.print_response_stream()


def main():
    documents = load_documents()
    client = create_qdrant_client()
    vector_store = create_vector_store(client)
    storage_context = create_storage_context(vector_store)
    llm = create_llama()
    service_context = create_service_context(llm)
    index = create_index(documents, service_context, storage_context)
    query_engine = create_query_engine(index)
    query = "Hi"
    response_stream = query_data(query_engine, query)
    print_response_stream(response_stream)


if __name__ == "__main__":
    main()
