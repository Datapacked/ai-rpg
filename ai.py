import requests

AI_MODEL = "deepseek-r1:1.5b"

IP = "127.0.0.1"
OLLAMA_PORT = 11434

GENERATE_API = f"http://{IP}:{OLLAMA_PORT}/api/generate"


def AI(prompt, context=False):
	if not context:
		ret = requests.post(
			GENERATE_API,
			json={
				"model": AI_MODEL,
				"prompt": "what is 2 + 4? remember the result",
				"stream": False,
				"keep_alive": "5m",
			},
		).json()
	else:
		a = requests.post(
			GENERATE_API,
			json={
				"model": AI_MODEL,
				"prompt": "what is 2 + 4? remember the result",
				"stream": False,
				"keep_alive": "5m",
				"context": context,
			},
		).json()
	
	return (ret["response"], ret["context"])


R = requests.post(
	GENERATE_API,
	json={
		"model": AI_MODEL,
		"prompt": "what is 2 + 4? remember the result",
		"stream": False,
		"keep_alive": "5m",
	},
).json()

print(R["response"])

print("--- --- ---")

R = requests.post(
	GENERATE_API,
	json={
		"model": AI_MODEL,
		"prompt": "what 3 times the result?",
		"stream": False,
		"context": R["context"],
	},
).json()

print(R["response"])
