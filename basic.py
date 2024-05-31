from llama_index.llms import Ollama

llm = Ollama(model="mistral", request_timeout=360)

prompt = "Hi in a few words"

response = llm.complete(prompt, True)
print(response)
