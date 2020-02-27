from .is_anagram import is_anagram
import pytest


@pytest.mark.parametrize("messageA, messageB", (
        ("test", "tset"),
        ("test", "test"),
        ("cart horse", "orchestra")
))
def test_is_anagram(messageA, messageB):
    assert is_anagram(messageA, messageB)


@pytest.mark.parametrize("messageA, messageB",(
        ("test", "not test"),
        ("not test", "test"),
        ("test", "tesssssst")
))
def test_is_not_anagram(messageA, messageB):
    assert not is_anagram(messageA, messageB)


def test_real_anagram():
    assert is_anagram("test", "tets")

