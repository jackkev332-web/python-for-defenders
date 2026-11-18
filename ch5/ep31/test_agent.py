from agent import FUNCTIONS, TOOLS, approve, block_ip, proposals


def test_every_tool_the_ai_is_offered_has_a_function():
    names = [tool["function"]["name"] for tool in TOOLS]
    assert names == list(FUNCTIONS)


def test_the_ai_can_only_propose_a_block(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert block_ip("203.0.113.45").startswith("Proposed")
    assert "203.0.113.45" in proposals
    assert not (tmp_path / "blocklist.txt").exists()


def test_our_own_users_are_never_blocked(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert block_ip("192.0.2.10").startswith("Refused")
    approve("192.0.2.31")
    assert not (tmp_path / "blocklist.txt").exists()


def test_a_person_can_block(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    approve("203.0.113.45")
    assert (tmp_path / "blocklist.txt").read_text() == "203.0.113.45\n"
