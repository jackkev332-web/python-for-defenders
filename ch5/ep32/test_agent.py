from agent import FUNCTIONS, TOOLS, approve, block_ip, proposals


def test_every_tool_the_ai_is_offered_has_a_function():
    names = [tool["function"]["name"] for tool in TOOLS]
    assert names == list(FUNCTIONS)


def test_the_ai_cannot_block_our_own_users(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert block_ip("192.0.2.10").startswith("Refused")
    assert "192.0.2.10" not in proposals
    assert not (tmp_path / "blocklist.txt").exists()


def test_every_decision_is_audited(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    block_ip("192.0.2.10")
    approve("203.0.113.45")
    events = [line[20:] for line in (tmp_path / "audit.log").read_text().splitlines()]
    assert events == ["the AI asked to block 192.0.2.10: refused, our user alice",
                      "a person blocked 203.0.113.45: added to blocklist.txt"]


def test_a_person_can_block(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    approve("203.0.113.45")
    assert (tmp_path / "blocklist.txt").read_text() == "203.0.113.45\n"
