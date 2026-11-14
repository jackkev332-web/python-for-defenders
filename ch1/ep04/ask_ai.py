"""Ask a free AI model running on your own computer to explain a Python error.

Usage:  python ask_ai.py error.txt
Needs Ollama (https://ollama.com) running, with the qwen3:8b model downloaded.
Temperature 0, a fixed seed and CPU-only make the answer repeatable
(graphics-card math can vary slightly from run to run).
"""
import json
import sys
import urllib.request

error = open(sys.argv[1]).read()
question = ("I'm learning Python. My script crashed with this error. In at most 3 short "
            "sentences, explain what it means and how to fix it.\n\n" + error)
request = urllib.request.Request(
    "http://localhost:11434/api/generate",
    data=json.dumps({"model": "qwen3:8b", "prompt": question, "stream": False, "think": False,
                     "keep_alive": 0,
                     "options": {"temperature": 0, "seed": 42, "num_gpu": 0}}).encode(),
    headers={"Content-Type": "application/json"})
answer = json.load(urllib.request.urlopen(request))["response"].strip()
print("AI says:")
print(answer)
