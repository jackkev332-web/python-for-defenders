"""Make year_auth.log: the synthetic practice day, repeated for every day of 2026.

Each copy gets that day's date; everything else is the same practice day (RFC 5737 documentation IPs).
Usage: python make_year_log.py     (needs practice_auth.log in this folder)
"""
from datetime import date, timedelta
from pathlib import Path

day = Path("practice_auth.log").read_text(encoding="utf-8").splitlines()
first = date(2026, 1, 1)
with open("year_auth.log", "w", encoding="utf-8", newline="\n") as out:
    for n in range(365):
        stamp = (first + timedelta(days=n)).isoformat()
        for line in day:
            out.write(stamp + line[10:] + "\n")
size = Path("year_auth.log").stat().st_size
print(f"year_auth.log: {365 * len(day):,} lines, {size / 1e6:.1f} MB")
