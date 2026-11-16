import json

with open("practice_journal.json") as log:
    first = log.readline()
entry = json.loads(first)
for key in entry:
    print(f"{key:<22} {entry[key]}")
