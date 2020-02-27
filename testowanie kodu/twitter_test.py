# import unittest
# from twitter import Twitter
# import pytest

# class TwitterTest(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.twitter = Twitter()
#
#     def test_initizalization(self):
#         self.assertTrue(self.twitter)
#
#     def test_tweet_single(self):
#         #Givev
#         #twitter = Twitter()
#         #When
#         self.twitter.tweet("Test message")
#         #Then
#         self.assertEqual(self.twitter.tweets, ["Test message"])
#
#
# if __name__ == "__main__":
#     unittest.main()

from twitter import Twitter
import pytest
import unittest.mock
import requests


class ResponseGetMock:

    def json(self):
        return {"awatar_url": "test"}


@pytest.fixture(params=[None, "Python"])
def username(request):
    return request.param


@pytest.fixture(params=["list", "backend"], name="twitter")
def fixture_twitter(backend, username, request, monkeypatch):
    if request.param == "list":
        twitter = Twitter(username=username)
    if request.param == "backend":
        twitter = Twitter(backend=backend, username=username)
    return twitter


def test_initialize_twoo_twitter_clases(backend):
    twitA = Twitter(backend=backend)
    twitB = Twitter(backend=backend)
    twitA.tweet("Test A")
    twitA.tweet("Test B")
    assert twitB.tweet_message == ["Test A", "Test B"]


def test_initizalization(twitter):
    return twitter


@unittest.mock.patch.object(Twitter, "get_user_awatar", return_value='test')
def test_tweet_single(awatar_mock, twitter):
    twitter.tweet("Message")
    assert twitter.tweet_message == ["Message"]


def test_tweet_long(twitter):
    with pytest.raises(Exception):
        twitter.tweet("Message" * 41)
    assert twitter.tweet_message == []


@pytest.mark.parametrize("message, expected", (
        ("test #first message", ["first"]),
        ("Test #TOO message", ["too"]),
        ("#message ", ["message"]),
        ("test #first and test #second", ["first", "second"])
))
def test_tweet_with_hashtags(twitter, message, expected):
    assert twitter.find_hashtags(message) == expected


@unittest.mock.patch.object(requests, "get", return_value=ResponseGetMock())
def test_tweet_with_username(username_mock, twitter):
    if not twitter.username:
        pytest.skip()

    twitter.tweet("Test message")
    assert twitter.tweets == [{"message": "Test message", "awatar": "test", "hashtags": []}]
    username_mock.assert_called()


@unittest.mock.patch.object(requests, "get", return_value=ResponseGetMock())
def test_tweet_with_hashtags_mock(username_mock, twitter):
    twitter.find_hashtags = unittest.mock.Mock()
    twitter.find_hashtags.return_value = ["first"]
    twitter.tweet("Test #second")
    assert twitter.tweets[0]["hashtags"] == ["first"]


def test_twitter_version(twitter):
    twitter.version = unittest.mock.MagicMock()
    twitter.version.__eq__.return_value = "2.0"
    assert twitter.version == "2.0"


@unittest.mock.patch.object(requests, "get", return_value=ResponseGetMock())
def test_tweet_get_all_hashtags(username_mock, twitter):
    twitter.tweet("test #first")
    twitter.tweet("test #first #second")
    twitter.tweet("test #third")
    assert twitter.get_all_hashtags() == {"first", "second", "third"}


@unittest.mock.patch.object(requests, "get", return_value=ResponseGetMock())
def test_tweet_get_all_hashtags_not_found(username_mock, twitter):
    twitter.tweet("test not found hashtag")
    assert twitter.get_all_hashtags() == "No hashtags found"