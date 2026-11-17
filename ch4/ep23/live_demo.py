# Live demo - Python for Defenders, episode 23
# A pretend server writes live_auth.log while the watchdog follows it.
import _thread
import threading
import time
from pathlib import Path

from watchdog import watch_live

DAY = Path("practice_auth.log").read_text().splitlines()


def pretend_server():
    time.sleep(1)                        # let the watchdog start following
    with open("live_auth.log", "a", buffering=1) as log:
        for number, line in enumerate(DAY, start=1):
            log.write(line + "\n")       # one whole line at a time
            if number % 100 == 0:
                time.sleep(0.05)
    time.sleep(1)                        # let the watchdog read the end
    _thread.interrupt_main()             # like pressing Ctrl+C


Path("live_auth.log").write_text("")
threading.Thread(target=pretend_server).start()
watch_live("live_auth.log", threshold=5)
