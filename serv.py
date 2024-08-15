import requests

url = "http://localhost:4891/v1/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer NO_API_KEY"
}
data = {
    "model": "C:\\LLM-Models\\kunoichi\\kunoichi-dpo-v2-7b.Q5_K_M.gguf",
    "prompt": "В LLM моделях есть параметры: temperature, max_tokens, top_p, n, stream?",
    "temperature": 0.7,
    "max_tokens": 4096,
    "top_p": 0.95,
    "n": 1,
    "stream": False
}

response = requests.post(url, headers=headers, json=data)

# Проверка успешности запроса и вывод результата
if response.status_code == 200:
    print("Ответ сервера:", response.json())
else:
    print(f"Ошибка: {response.status_code}")
    print("Детали ошибки:", response.text)
