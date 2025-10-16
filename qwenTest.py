from openai import OpenAI

# Conectamos el cliente al endpoint local de Ollama
client = OpenAI(
    base_url="http://localhost:11434/v1",  # API local de Ollama
    api_key="ollama"  # no se usa, pero el cliente lo requiere
)

# Generar texto con el modelo Qwen2.5
response = client.chat.completions.create(
    model="qwen2.5",
    messages=[
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": "Explícame qué es Docker Compose."}
    ]
)

print(response.choices[0].message.content)
