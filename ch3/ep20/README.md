# Episode 20 — Machine learning: unusual is not malicious

Python for Defenders · Chapter 3: Real servers (Intermediate)

Video: coming soon

## First: install scikit-learn (once, inside your virtual environment — episode 11)

- `python -m pip install scikit-learn`
- The expected output below came from scikit-learn 1.9.1; other versions may score a little differently.

## Also try

- `python scanners.py access.log` — episode 17's rule (10+ 404s) flags only the two scanners
- Change `random_state=0` to `42` in `unusual.py`: one more visitor tips over the line

## Run it

Open a terminal **in this folder**, then:

- Windows: `python unusual.py access.log`
- macOS / Linux: `python3 unusual.py access.log`

Expected output:

```
IP ADDRESS       REQS  404s  PATHS   SCORE
198.51.100.200     30    30     30  -0.867  unusual
203.0.113.45       21    21      3  -0.798  unusual
198.51.100.50      10     2     10  -0.722  unusual
192.0.2.29          8     1      8  -0.616  unusual
192.0.2.59          6     0      4  -0.498  
192.0.2.16          7     1      7  -0.482  

4 of 63 IPs look unusual
```

## Files

- `unusual.py`
- `scanners.py`
- `access.log`

## Challenge

Add a fourth number per IP, like how many POST requests it sent, and see who moves up. Share yours in the comments.
