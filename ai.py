import requests, time

AI_MODEL = "deepseek-r1:1.5b"

IP = "127.0.0.1"
OLLAMA_PORT = 11434

GENERATE_API = f"http://{IP}:{OLLAMA_PORT}/api/generate"

# AI function to ask AI, with context optionally

def AI(prompt, context=False):
	if not context:
		ret = requests.post(
			GENERATE_API,
			json={
				"model": AI_MODEL,
				"prompt": prompt,
				"stream": False,
				"keep_alive": "5m",
			},
		).json()
	else:
		a = requests.post(
			GENERATE_API,
			json={
				"model": AI_MODEL,
				"prompt": prompt,
				"stream": False,
				"keep_alive": "5m",
				"context": context,
			},
		).json()
	
	return (ret["response"], ret["context"])


# neutered code because im too lazy to comment block it

if False:
	R = requests.post(
		GENERATE_API,
		json={
			"model": AI_MODEL,
			"prompt": "what is 2 + 4? remember the result",
			"stream": False,
			"keep_alive": "10s",
		},
	).json()

	print(R["response"])

	print("--- --- ---")
	time.sleep(20)
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
