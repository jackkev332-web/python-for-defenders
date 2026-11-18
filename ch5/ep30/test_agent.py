from agent import FUNCTIONS, TOOLS, check, ip_details, recent_failures


def test_every_tool_the_ai_is_offered_has_a_function():
    names = [tool["function"]["name"] for tool in TOOLS]
    assert names == list(FUNCTIONS)


def test_ip_details_for_the_worst_attacker():
    details = ip_details("203.0.113.45")
    assert details.startswith("203.0.113.45: 212 failed logins")


def test_recent_failures_returns_n_lines():
    assert len(recent_failures(5).splitlines()) == 5


def test_the_check_wants_the_worst_attacker_first():
    assert check("Deal with 203.0.113.45 first.") is None
    assert "Check failed" in check("Deal with 203.0.113.9 first.")
