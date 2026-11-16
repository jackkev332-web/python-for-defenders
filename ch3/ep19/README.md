# Episode 19 — Secrets scanner: catch leaked keys before you share

Python for Defenders · Chapter 3: Real servers (Intermediate)

Video: coming soon

## First: make the practice project

- `python make_demo_project.py` writes `demo_project/`: 7 files with **fake** secrets (AWS's documentation
  example key, and keys labeled FAKE). They're glued together when the script runs, so this repository
  itself never contains a secret-shaped string.

## Also try

- `python suffixes.py` — why `.env` has no suffix
- `python scanner.py .` on your own project folder (it never prints the secret, only where it is)

## Run it

Open a terminal **in this folder**, then:

- Windows: `python scanner.py demo_project`
- macOS / Linux: `python3 scanner.py demo_project`

Expected output:

```
.env:1  AWS access key ID
app/config.py:3  password in code
app/settings.json:3  GitHub token
deploy/id_demo:1  private key

4 possible secrets in 7 files
```

## Files

- `scanner.py`
- `make_demo_project.py`
- `suffixes.py`

## Challenge

Line 2 of .env holds an AWS secret key with no fixed prefix. Make the scanner catch it too. Share yours in the comments.
