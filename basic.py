from llama_index.llms import Ollama

llm = Ollama(model="mistral", request_timeout=360)

prompt = "Hi"

response = llm.complete(prompt, True)
print(response)
