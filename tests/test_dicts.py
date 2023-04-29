from utils.dicts import get_val


def test_get_val():
    assert get_val({"vcs": "mercurial"}, "git", "test") == "test"
    assert get_val(("vcs", "mercurial"), "git", "test") == "Недопустимая коллекция"
    assert get_val({"vcs": "mercurial"}, "test") == "git"
    assert get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
