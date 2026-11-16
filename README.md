# Python for Defenders

Learn Python from zero by building a real defensive security tool: a log watchdog that
gains one feature per episode, from your first script to an AI-assisted analyst.

Series trailer: https://youtu.be/wD-6ig3VVv0

## Episodes

| # | Episode | Level | Code | Video |
|---|---|---|---|---|
| 1 | Your first Python script: read a server log | Novice | [ch1/ep01](ch1/ep01) | [watch](https://youtu.be/7XWZmS8Xaio) |
| 2 | Strings and if: is this a failed login? | Novice | [ch1/ep02](ch1/ep02) | [watch](https://youtu.be/4DENK-4qAEs) |
| 3 | Loops: check all 1,528 lines | Novice | [ch1/ep03](ch1/ep03) | [watch](https://youtu.be/z_LfXlipr4w) |
| 4 | Errors and AI: read the red text, then check the AI | Novice | [ch1/ep04](ch1/ep04) | [watch](https://youtu.be/-7y-7skhn-w) |
| 5 | Split strings: who is attacking? | Novice | [ch1/ep05](ch1/ep05) | [watch](https://youtu.be/qRs0K45AMrY) |
| 6 | Dictionaries: count attacks per IP | Novice | [ch1/ep06](ch1/ep06) | [watch](https://youtu.be/RbySNpZs8z8) |
| 7 | Functions: Watchdog v1.0 | Novice | [ch1/ep07](ch1/ep07) | [watch](https://youtu.be/GBdoB1Hg1Oo) |
| 8 | Counter: count anything in one line | Beginner | [ch2/ep08](ch2/ep08) | [watch](https://youtu.be/yYvzWLXnwpM) |
| 9 | Sets and f-strings: a real report table | Beginner | [ch2/ep09](ch2/ep09) | [watch](https://youtu.be/GdwFqgVMtfE) |
| 10 | Regex: match a log line by its shape | Beginner | [ch2/ep10](ch2/ep10) | [watch](https://youtu.be/jyb4WStTJXw) |
| 11 | Virtual environments: install tools safely | Beginner | [ch2/ep11](ch2/ep11) | [watch](https://youtu.be/mqX8oFhz8zk) |
| 12 | pytest: prove your watchdog works | Beginner | [ch2/ep12](ch2/ep12) | coming soon |
| 13 | AI writes the regex, pytest judges it | Beginner | [ch2/ep13](ch2/ep13) | coming soon |
| 14 | argparse: Watchdog v2.0, a real command-line tool | Beginner | [ch2/ep14](ch2/ep14) | coming soon |
| 15 | datetime: when did each attack happen? | Intermediate | [ch3/ep15](ch3/ep15) | coming soon |

## How to use

1. Install Python 3 from https://www.python.org/downloads/
2. Download this repository: green **Code** button → **Download ZIP**, then unzip it.
3. Open a terminal in an episode folder and follow that folder's README.

## About the data

`practice_auth.log` is synthetic. Every IP address comes from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24,
RFC 5737), so no real system is named. Only analyze real logs from systems you administer.

## License

MIT — see [LICENSE](LICENSE).
