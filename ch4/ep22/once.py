from watchdog import find_lines, read_log

lines = list(read_log("practice_auth.log"))
print(len(find_lines(lines, "Failed password")), "failed logins")
print(len(find_lines(lines, "Accepted")), "accepted logins")
