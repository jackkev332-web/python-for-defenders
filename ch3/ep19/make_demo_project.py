"""Make demo_project/: a tiny made-up project with FAKE secrets in it, for a secrets-scanner lesson.

Every key is fake. The AWS pair is the example pair from AWS's own documentation; the token, the
private key and the password are labelled FAKE. They are glued together at runtime (prefix + rest),
so this file itself never contains a secret-shaped string: GitHub scans pushed code for keys too.

Usage: python make_demo_project.py
"""
from pathlib import Path

AWS_KEY_ID = "AKIA" + "IOSFODNN7EXAMPLE"                        # AWS documentation's example ID
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/" + "bPxRfiCYEXAMPLEKEY"     # ... and its example secret
GITHUB_TOKEN = "ghp" + "_" + "THISISAFAKETOKENFORAPYTHONLESSON0000"
KEY_BEGIN = "-----BEGIN " + "PRIVATE KEY-----"
KEY_END = "-----END " + "PRIVATE KEY-----"

FILES = {
    "notes.md": "# Demo app\n\nA made-up project for a Python lesson. Every key in it is FAKE.\n",
    "app/main.py": 'from app.config import DB_HOST\n\nprint("Connecting to", DB_HOST)\n',
    "app/config.py": 'DB_HOST = "db.example.com"\nDB_USER = "app"\nDB_PASSWORD = ' + '"fake-password-for-a-lesson"\n',
    "app/settings.json": '{\n  "site": "www.example.com",\n  "deploy_token": "' + GITHUB_TOKEN + '"\n}\n',
    ".env": "AWS_ACCESS_KEY_ID=" + AWS_KEY_ID + "\nAWS_SECRET_ACCESS_KEY=" + AWS_SECRET + "\n",
    "deploy/id_demo": KEY_BEGIN + "\nTHIS-IS-A-FAKE-KEY-FOR-A-PYTHON-LESSON\n" + KEY_END + "\n",
}
LOGO = b"\x89PNG\r\n\x1a\n" + bytes([0, 255, 128, 7] * 16)      # a few binary bytes, like a picture


def main() -> None:
    root = Path("demo_project")
    for name, text in FILES.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
    (root / "static").mkdir(exist_ok=True)
    (root / "static" / "logo.png").write_bytes(LOGO)
    print("demo_project/ written: 7 files, every key FAKE")


if __name__ == "__main__":
    main()
