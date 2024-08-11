import ollama

client = ollama.Client()

stream = ollama.chat(
    model="llama3.1",
    messages=[{
        "role":"user",
        "content":"Do u remember what i've asked u "}],
    stream=True
)
for chunk in stream:
    print(chunk["message"]["content"],end ="",flush=True)