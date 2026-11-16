"""Run the tests, and send the AI its own regex plus pytest's failures: can it fix it?"""
import json
import subprocess
import sys
import urllib.request

regex = open("ai_regex.txt").read().strip()
result = subprocess.run([sys.executable, "-m", "pytest", "-q"], capture_output=True, text=True)
failures = [l for l in result.stdout.splitlines() if l.startswith("FAILED")]

question = ("Your regex failed my tests. Here is the regex:\n" + regex +
            "\n\nAnd here is what pytest says:\n" + "\n".join(failures) +
            "\n\nFix the regex. Reply with only the regex.")
request = urllib.request.Request(
    "http://localhost:11434/api/generate",
    data=json.dumps({"model": "qwen3:8b", "prompt": question, "stream": False, "think": False,
                     "keep_alive": 0,
                     "options": {"temperature": 0, "seed": 42, "num_gpu": 0}}).encode(),
    headers={"Content-Type": "application/json"})
answer = json.load(urllib.request.urlopen(request))["response"].strip()
print("Failures sent to the AI:", len(failures))
print("AI says:")
print(answer)
print("Same regex as before:", answer == regex)
