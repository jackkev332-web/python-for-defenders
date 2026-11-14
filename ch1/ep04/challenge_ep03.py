print("Watchdog starting")
with open("practice_auth.log") as log:
    text = log.read()
lines = text.splitlines()
print("Lines in log:", len(lines))

failures = []
for line in lines:
    if "Failed password" in line:
        failures.append(line)
print("Failed logins:", len(failures))

successes = []
for line in lines:
    if "Accepted" in line:
        successes.append(line)
print("Successful logins:", len(successes))
