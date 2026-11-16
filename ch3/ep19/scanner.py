# Secrets scanner - Python for Defenders, chapter 3 (episode 19)
import argparse
import re
import sys
from pathlib import Path

PATTERNS = {
    "AWS access key ID": re.compile(r"AKIA[0-9A-Z]{16}"),
    "GitHub token": re.compile(r"ghp_[A-Za-z0-9]{36}"),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "password in code": re.compile(r'password\s*=\s*"[^"]+"', re.I),
}


def main():
    parser = argparse.ArgumentParser(
        description="Look for secrets before you share a folder.")
    parser.add_argument("folder", help="the folder to scan")
    args = parser.parse_args()

    root = Path(args.folder)
    files = 0
    found = 0
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        files = files + 1
        text = path.read_text(encoding="utf-8", errors="ignore")
        for number, line in enumerate(text.splitlines(), start=1):
            for kind, pattern in PATTERNS.items():
                if pattern.search(line):
                    where = path.relative_to(root).as_posix()
                    print(f"{where}:{number}  {kind}")
                    found = found + 1
    print()
    print(f"{found} possible secrets in {files} files")
    if found > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
