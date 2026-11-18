"""How much memory do the rules need for a year of logs? Episode 25's way vs v4.0's one pass.

Usage: python memory.py     (needs year_auth.log: run python make_year_log.py first)
"""
import contextlib
import io
import tracemalloc

from watchdog import apply_rules, load_rules, read_log

LOG = "year_auth.log"
rules = load_rules("rules.toml")


def peak_mb(task):
    tracemalloc.start()
    with contextlib.redirect_stdout(io.StringIO()):
        task()
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return peak / 1e6


logs = {}
episode_25 = peak_mb(lambda: logs.update(auth=list(read_log(LOG))))   # what episode 25 did
v4 = peak_mb(lambda: apply_rules(rules, {"auth": LOG}))
print(f"{LOG}: {len(logs['auth']):,} lines")
print(f"episode 25, all lines in a list: {episode_25:7.2f} MB peak")
print(f"v4.0, one pass over the file:   {v4:7.2f} MB peak")
