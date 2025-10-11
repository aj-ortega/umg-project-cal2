from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="not-needed")

with client.chat.completions.stream(
    model="deepseek-r1",
    messages=[
        {"role": "system", "content": "Solo muestra los pasos y fórmulas, no expliques."},
        {"role": "user", "content": "∫ x^2 * e^x dx"}
    ],
) as stream:
    for event in stream:
        if event.type == "message.delta" and event.delta.content:
            print(event.delta.content, end="", flush=True)

