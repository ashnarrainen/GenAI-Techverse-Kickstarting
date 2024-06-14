### Input Section

1. **Loading Documents:**
   ```python
   documents = SimpleDirectoryReader("./data").load_data(True)
   ```
   - `SimpleDirectoryReader` is a utility to read documents from a specified directory (`./data`).
   - The `load_data(True)` method is called to load the documents from this directory.
   - `documents` will now contain the data read from the directory, which will be used later for indexing.

### Setup Storage Context

2. **Initializing Qdrant Client and Vector Store:**
   ```python
   qdrant_client = QdrantClient(path="./qdrant_data")
   qdrant_store = QdrantVectorStore("customized_data", qdrant_client)
   storage_context = StorageContext.from_defaults(vector_store=qdrant_store)
   ```
   - `QdrantClient` is initialized with a specified path (`./qdrant_data`). Qdrant is a vector database used to store and retrieve vector embeddings efficiently.
   - `QdrantVectorStore` is created with a name ("customized_data") and the Qdrant client. This is where the vectors (embeddings) will be stored.
   - `StorageContext.from_defaults(vector_store=qdrant_store)` creates a storage context using the vector store created above. This context will be used to store and manage the vectors during processing.

### Processing Section

3. **Setting up the Language Model and Service Context:**

   ```python
   llm = Ollama(model="mistral", request_timeout=360)
   service_context = ServiceContext.from_defaults(llm=llm, embed_model="local")
   ```

   - `Ollama(model="mistral", request_timeout=360)` initializes a language model (`Ollama`) with the specified model name ("mistral") and a request timeout of 360 seconds. This language model will be used for generating responses to queries.
   - `ServiceContext.from_defaults(llm=llm, embed_model="local")` creates a service context with the specified language model and embedding model ("local"). The service context integrates the language model and the embedding model, which will be used for processing documents and queries.

4. **Creating the Vector Store Index:**
   ```python
   index = VectorStoreIndex.from_documents(
       documents, service_context=service_context, storage_context=storage_context
   )
   ```
   - `VectorStoreIndex.from_documents` creates an index from the loaded documents using the service context and storage context. This index is essentially a searchable representation of the documents, where each document is converted into a vector embedding and stored in the vector store.

### Output Section

5. **Setting Up the Query Engine:**

   ```python
   query_engine = index.as_query_engine(streaming=True)
   ```

   - `index.as_query_engine(streaming=True)` sets up a query engine that can process queries against the indexed documents. The `streaming=True` parameter indicates that the responses will be streamed back as they are generated.

6. **Querying and Printing the Response:**
   ```python
   query = promp
   response_stream = query_engine.query(query)
   response_stream.print_response_stream()
   ```
   - `query = promp` sets the query string (assuming `promp` is a variable holding the user's query).
   - `query_engine.query(query)` processes the query using the query engine, generating a response stream.
   - `response_stream.print_response_stream()` prints the responses from the stream as they are generated.

### Summary

- **Document Loading:** Reads documents from a specified directory.
- **Storage Context Setup:** Configures a vector database (Qdrant) to store vector embeddings of the documents.
- **Processing Setup:** Initializes a language model and service context for generating embeddings and responses.
- **Index Creation:** Converts documents into vector embeddings and creates an index for efficient querying.
- **Query Engine Setup:** Configures a query engine to process user queries against the indexed documents.
- **Query Execution:** Executes the query and streams the response.

### What are Vectors?

Vectors, in the context of machine learning and natural language processing (NLP), are numerical representations of data. They are essentially arrays of numbers that encode information in a format that a machine learning model can process.

For example, in NLP:

Words, sentences, or entire documents can be converted into vectors.
These vectors capture semantic information, meaning they represent the meaning or context of the text they encode.
