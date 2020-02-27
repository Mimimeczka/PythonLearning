import pytest


@pytest.fixture()
def backend(tmpdir):
    temp_file = tmpdir.join("testy.txt")
    temp_file.write("")
    return temp_file


@pytest.fixture(autouse=True)
def no_request(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")