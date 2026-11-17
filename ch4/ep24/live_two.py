# Live demo - Python for Defenders, episode 24
# Pretend servers write an SSH log and a web log, hour by hour, while the watchdog follows both.
import asyncio
import threading
import time
from pathlib import Path

from watchdog import watch_live

SSH = Path("practice_auth.log").read_text().splitlines()
WEB = Path("access.log").read_text().splitlines()


def pretend_servers():
    time.sleep(1)                              # let the watchdog start following
    with open("live_auth.log", "a", buffering=1) as ssh, \
         open("live_access.log", "a", buffering=1) as web:
        for hour in range(24):
            for line in SSH:
                if int(line[11:13]) == hour:     # 2026-11-09T03:...
                    ssh.write(line + "\n")
            for line in WEB:
                if int(line.split(":")[1]) == hour:   # [09/Nov/2026:03:...
                    web.write(line + "\n")
            time.sleep(0.25)                   # one hour of logs every quarter second


Path("live_auth.log").write_text("")
Path("live_access.log").write_text("")
threading.Thread(target=pretend_servers).start()
print("following live_auth.log and live_access.log for 9 seconds")
asyncio.run(watch_live("live_auth.log", "live_access.log", 5, seconds=9))
