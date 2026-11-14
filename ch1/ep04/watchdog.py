print("Watchdog starting")
try:
    with open("practice_auth.log") as log:
        text = log.read()
except FileNotFoundError:
    raise SystemExit("Can't find practice_auth.log. Open your terminal in its folder.")
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
