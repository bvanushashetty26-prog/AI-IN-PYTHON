
import ollama

message = [
    {
        "role": "system",
        "content": "You are a funny assistant. Give short, funny replies in simple English."
    },
    {
        "role": "user",
        "content": "What is AI?"
    }
]

model_name = "llama3.2:latest"

response = ollama.chat(
    model=model_name,
    messages=message
)

print(response["message"]["content"])
