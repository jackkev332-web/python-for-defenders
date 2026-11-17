from watchdog import FAILED, find_lines, read_log

LINES = list(read_log("practice_auth.log"))
FAILURES = find_lines(LINES, "Failed password")
ACCEPTED = find_lines(LINES, "Accepted")


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
