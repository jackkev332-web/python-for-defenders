# How many failed logins came after 04:00? - Python for Defenders, episode 15
from datetime import datetime, timezone

from timeline import get_time
from watchdog import find_lines, read_log

cutoff = datetime(2026, 11, 9, 4, 0, tzinfo=timezone.utc)
count = 0
for line in find_lines(read_log("practice_auth.log"), "Failed password"):
    if get_time(line) >= cutoff:
        count = count + 1
print(count, "failed logins after 04:00 UTC")
