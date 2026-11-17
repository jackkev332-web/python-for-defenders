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
| 12 | pytest: prove your watchdog works | Beginner | [ch2/ep12](ch2/ep12) | [watch](https://youtu.be/obpk-Ctx8V0) |
| 13 | AI writes the regex, pytest judges it | Beginner | [ch2/ep13](ch2/ep13) | [watch](https://youtu.be/hyBv4_yaoJ8) |
| 14 | argparse: Watchdog v2.0, a real command-line tool | Beginner | [ch2/ep14](ch2/ep14) | [watch](https://youtu.be/fP_4g-Pa3pM) |
| 15 | datetime: when did each attack happen? | Intermediate | [ch3/ep15](ch3/ep15) | [watch](https://youtu.be/5YK0hZ5g8n0) |
| 16 | JSON logs: read the systemd journal | Intermediate | [ch3/ep16](ch3/ep16) | [watch](https://youtu.be/NWULJRamhEU) |
| 17 | Web server logs: who is scanning your site? | Intermediate | [ch3/ep17](ch3/ep17) | [watch](https://youtu.be/cSXS2s2cfXc) |
| 18 | Alerts: let the watchdog call you | Intermediate | [ch3/ep18](ch3/ep18) | [watch](https://youtu.be/2HtjPcrm-dY) |
| 19 | Secrets scanner: catch leaked keys before you share | Intermediate | [ch3/ep19](ch3/ep19) | [watch](https://youtu.be/0Y_EK-69WiI) |
| 20 | Machine learning: unusual is not malicious | Intermediate | [ch3/ep20](ch3/ep20) | [watch](https://youtu.be/GKjowgwvByM) |
| 21 | Watchdog v3.0: one tool, two logs (chapter 3 finale) | Intermediate | [ch3/ep21](ch3/ep21) | coming soon |
| 22 | Generators: a year of logs, almost no memory | Advanced | [ch4/ep22](ch4/ep22) | coming soon |
| 23 | Follow a log live: alerts the moment they happen | Advanced | [ch4/ep23](ch4/ep23) | coming soon |
| 24 | asyncio: watch two logs at once | Advanced | [ch4/ep24](ch4/ep24) | coming soon |
| 25 | Rules as data: change the rules, not the code | Advanced | [ch4/ep25](ch4/ep25) | coming soon |

## How to use

1. Install Python 3 from https://www.python.org/downloads/
2. Download this repository: green **Code** button → **Download ZIP**, then unzip it.
3. Open a terminal in an episode folder and follow that folder's README.

## About the data

`practice_auth.log` is synthetic. Every IP address comes from the documentation ranges (192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24,
RFC 5737), so no real system is named. Only analyze real logs from systems you administer.

## License

MIT — see [LICENSE](LICENSE).
