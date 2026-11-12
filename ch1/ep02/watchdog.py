print("Watchdog starting")
with open("practice_auth.log") as log:
    text = log.read()
lines = text.splitlines()
print("Lines in log:", len(lines))

number = 186
line = lines[number]
if "Failed password" in line:
    print("Line", number, "ALERT: failed login")
else:
    print("Line", number, "ok")
