from ai_summary import mentions
from watchdog import FAILED, find_lines, get_ip, read_log

LINES = list(read_log("practice_auth.log"))
FAILURES = find_lines(LINES, "Failed password")
ACCEPTED = find_lines(LINES, "Accepted")

# Hostile lines, written the way sshd writes them.
# The username is whatever the client sent.
FRAMED = ("2026-11-09T09:14:05.906646+00:00 web01 sshd[14287]: "
          "Failed password for invalid user "
          "admin from 192.0.2.10 port 22 "
          "from 198.51.100.66 port 64487 ssh2")
TRICK = ("2026-11-09T09:14:03.691522+00:00 web01 sshd[14287]: "
         "Invalid user Failed password for root from 192.0.2.10 port 22 ssh2 "
         "from 198.51.100.66 port 64487")


def test_matches_all_369_failures():
    matched = 0
    for line in FAILURES:
        if FAILED.search(line):
            matched = matched + 1
    assert matched == 369


def test_ip_is_the_word_after_from():
    for line in FAILURES:
        words = line.split()
        assert FAILED.search(line)["ip"] == words[words.index("from") + 1]


def test_user_is_the_word_before_from():
    for line in FAILURES:
        words = line.split()
        assert FAILED.search(line)["user"] == words[words.index("from") - 1]


def test_accepted_lines_do_not_match():
    for line in ACCEPTED:
        assert FAILED.search(line) is None


def test_cannot_be_framed():
    assert get_ip(FRAMED) == "198.51.100.66"
    user = FAILED.search(FRAMED)["user"]
    assert user == "admin from 192.0.2.10 port 22"


def test_a_line_that_does_not_match_is_skipped():
    assert get_ip(TRICK) is None


def test_check_passes_a_summary_with_every_address_and_count():
    summary = "203.0.113.45 - 212 failed logins, 203.0.113.77 - 8 failed logins"
    assert mentions(summary, "203.0.113.45", "212")
    assert mentions(summary, "203.0.113.77", "8")


def test_check_catches_a_missing_or_wrong_count():
    summary = "No attacks today, all clear. 203.0.113.77 tried a few times."
    assert not mentions(summary, "203.0.113.45", "212")
    assert not mentions(summary, "203.0.113.77", "8")


def test_every_rule_sees_every_line(capsys):
    from watchdog import apply_rules, load_rules
    apply_rules(load_rules("rules.toml"), {"auth": "practice_auth.log", "web": "access.log"})
    assert "8 hits from 3 rules" in capsys.readouterr().out
