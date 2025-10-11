# project python to use for deepseek 
import requests

url = "http://localhost:11434/api/generate"
data = {
    "model": "deepseek-r1",
    "prompt": "Explica brevemente qué es el teorema de Bayes."
}

response = requests.post(url, json=data, stream=True)

for line in response.iter_lines():
    if line:
        print(line.decode('utf-8'))

