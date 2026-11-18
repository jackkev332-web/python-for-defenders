from agent import TOOLS, watchdog_report


def test_the_tool_returns_the_watchdog_report():
    report = watchdog_report()
    assert report.startswith("IP ADDRESS")
    assert "203.0.113.45       212" in report


def test_the_ai_is_offered_exactly_one_tool():
    names = [tool["function"]["name"] for tool in TOOLS]
    assert names == ["watchdog_report"]
