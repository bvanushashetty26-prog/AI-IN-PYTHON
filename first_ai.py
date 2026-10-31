import ollama
model_name="llama3.2:latest"
prompt="how work the ollama"
response = ollama.generate (model = model_name,
                            prompt = prompt)
print(response.response)