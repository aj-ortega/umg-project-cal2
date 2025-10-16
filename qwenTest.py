from openai import OpenAI

# Cliente apuntando a tu Ollama local
client = OpenAI(
    base_url="http://localhost:11434/v1",  # API de Ollama
    api_key="ollama"  # No se valida, solo requerido por la librería
)

print("💬 Generando respuesta...\n")

# Hacemos la petición en modo streaming
with client.chat.completions.stream(
    model="qwen2.5",
    messages=[
        {"role": "system", "content": "Eres un asistente útil que responde en español."},
        {"role": "user", "content": "Explícame brevemente cómo funciona Docker Compose."}
    ],
) as stream:
    for event in stream:
        if event.type == "message.delta" and event.delta.content:
            print(event.delta.content, end="", flush=True)
    print()  # Salto de línea final

