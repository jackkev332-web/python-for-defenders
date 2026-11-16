from watchdog import find_lines, get_ip, get_user, read_log

NORMAL = "Failed password for root from 203.0.113.45"
INVALID = "Failed password for invalid user admin from 198.51.100.77"


def test_get_ip_from_a_normal_line():
    assert get_ip(NORMAL) == "203.0.113.45"


def test_invalid_user_line():
    assert get_user(INVALID) == "admin"
    assert get_ip(INVALID) == "198.51.100.77"


def test_finds_all_369_failures():
    lines = read_log("practice_auth.log")
    failures = find_lines(lines, "Failed password")
    assert len(failures) == 369
