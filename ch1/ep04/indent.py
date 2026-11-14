print("Watchdog starting")
with open("practice_auth.log") as log:
    text = log.read()
lines = text.splitlines()

failures = []
for line in lines:
if "Failed password" in line:
    failures.append(line)
