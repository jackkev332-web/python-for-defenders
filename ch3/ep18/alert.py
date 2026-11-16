# Alert - Python for Defenders, chapter 3 (episode 18)
import subprocess
import sys
from pathlib import Path

WATCHDOG = Path(__file__).parent / "watchdog.py"

result = subprocess.run([sys.executable, WATCHDOG] + sys.argv[1:],
                        capture_output=True, text=True)
code = result.returncode
print("watchdog exit code:", code)
if code == 0:
    print("OK: no suspicious IPs")
elif code == 1:
    print("ALERT: suspicious IPs found")
    print(result.stdout, end="")
else:
    print("ERROR: the watchdog itself failed")
    print(result.stderr, end="")
