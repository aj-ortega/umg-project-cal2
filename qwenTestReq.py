import requests
import json

URL = "http://localhost:11434/api/generate"
HEADERS = {"Content-Type": "application/json"}

prompt = "Hola, dime cómo estás hoy."

data = {
    "model": "qwen2.5",
    "prompt": prompt,
    "stream": True  # muy importante para que Ollama haga streaming
}

print("💬 Generando respuesta...\n")

# Petición POST con stream=True
with requests.post(URL, headers=HEADERS, json=data, stream=True) as r:
    r.raise_for_status()
    for line in r.iter_lines():
        if line:
            # Cada línea es un JSON con "response" parcial
            obj = json.loads(line.decode("utf-8"))
            fragment = obj.get("response", "")
            if fragment:
                print(fragment, end="", flush=True)
            if obj.get("done"):
                break  # termina cuando Ollama envía done=True

print("\n\n✅ Respuesta completada.")

