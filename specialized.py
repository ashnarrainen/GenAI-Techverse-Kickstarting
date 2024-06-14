from qdrant_client import QdrantClient
from llama_index import VectorStoreIndex, ServiceContext, SimpleDirectoryReader
from llama_index.llms import Ollama
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore

promp = "write me an sql query that gives the top 3 best students for each module in mauritius"


def main():
    # Input
    documents = SimpleDirectoryReader("./data").load_data(True)

    qdrant_client = QdrantClient(path="./qdrant_data")
    qdrant_store = QdrantVectorStore("customized_data", qdrant_client)
    storage_context = StorageContext.from_defaults(vector_store=qdrant_store)

    # Process
    llm = Ollama(model="mistral", request_timeout=360)
    service_context = ServiceContext.from_defaults(llm=llm, embed_model="local")
    index = VectorStoreIndex.from_documents(
        documents, service_context=service_context, storage_context=storage_context
    )

    # Output
    query_engine = index.as_query_engine(streaming=True)
    query = promp
    response_stream = query_engine.query(query)
    response_stream.print_response_stream()


if __name__ == "__main__":
    main()
