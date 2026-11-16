import re

PATTERN = re.compile(
    r"for (invalid user )?(?P<user>\S+) from (?P<ip>\S+)"
)

with open("practice_auth.log") as log:
    lines = log.read().splitlines()

failures = 0
matched = 0
for line in lines:
    if "Failed password" in line:
        failures = failures + 1
        if PATTERN.search(line):
            matched = matched + 1

print("Failed logins:", failures)
print("Matched:", matched)
