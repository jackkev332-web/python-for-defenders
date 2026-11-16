"""Ask a free AI model on your own computer to write the regex for a failed SSH login.

Needs Ollama (https://ollama.com) running, with the qwen3:8b model downloaded.
Temperature 0, a fixed seed and CPU-only make the answer repeatable.
The answer is saved to ai_regex.txt so you can paste it into watchdog.py.
"""
import json
import urllib.request

lines = open("practice_auth.log").read().splitlines()
normal = next(l for l in lines if "Failed password for " in l and "invalid user" not in l)
invalid = next(l for l in lines if "Failed password for invalid user" in l)

question = (
    "Write a Python regular expression that matches failed SSH "
    "login lines like these two, and captures the username as a "
    "named group called user and the IP address as a named "
    "group called ip. Reply with only the regex.\n\n"
    + normal + "\n" + invalid
)
request = urllib.request.Request(
    "http://localhost:11434/api/generate",
    data=json.dumps({"model": "qwen3:8b", "prompt": question, "stream": False, "think": False,
                     "keep_alive": 0,
                     "options": {"temperature": 0, "seed": 42, "num_gpu": 0}}).encode(),
    headers={"Content-Type": "application/json"})
answer = json.load(urllib.request.urlopen(request))["response"].strip()
open("ai_regex.txt", "w").write(answer + "\n")
print("AI says:")
print(answer)
