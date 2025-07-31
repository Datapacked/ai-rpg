import requests

IP = "127.0.0.1"
OLLAMA_PORT = 11434

GENERATE_API = f"http://{IP}:{OLLAMA_PORT}/api/generate"

R = requests.post(GENERATE_API, json={
	"model": "deepseek-r1:1.5b",
	"prompt": "what is 2 + 4? remember the result",
	"stream": False,
	"keep_alive": "5m"
}).json()

print(R["response"])

print("--- --- ---")

R = requests.post(GENERATE_API, json={
	"model": "deepseek-r1:1.5b",
	"prompt": "what 3 times the result?",
	"stream": False,
	"context": R["context"]
}).json()

print(R["response"])