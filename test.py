import requests

resp = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "deepseek-r1", "prompt": "Explica la integral de 1/(1+x^2)."},
    stream=True
)

for line in resp.iter_lines():
    if line:
        print(line.decode("utf-8"))