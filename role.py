import ollama


message = [
    {
        "role" : "system",
        "content": "you are funny hassan auto drive.reply in line"
    },
    {
        "role":"user",
        "content":"what is ai?"
    }
   
]
model_name = "llama3.2:latest"

response = ollama.chat(
    model=model_name,
    message=message)
print(response["message"]["content"])