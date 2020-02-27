import re
import os
import json
import urllib.parse
import requests

USERS_API = "https://api.github.com/users/"


class Twitter:
    version = "1.0"

    def __init__(self, backend=None, username=None):
        self.backend = backend
        self.__tweets = []
        self.username = username

    @property
    def tweets(self):
        if self.backend and not self.__tweets:
            backend_text = self.backend.read()
            if backend_text:
                self.__tweets = json.loads(backend_text)
        return self.__tweets

    @property
    def tweet_message(self):
        return [tweet["message"] for tweet in self.tweets]

    def get_user_awatar(self):
        if not self.username:
            return None
        url = urllib.parse.urljoin(USERS_API, self.username)
        resp = requests.get(url)
        return resp.json()["awatar_url"]

    def tweet(self, message):
        if len(message) > 160:
            raise Exception("Message to long")
        self.tweets.append({"message": message,
                            "awatar": self.get_user_awatar(),
                            "hashtags": self.find_hashtags(message)})
        if self.backend:
            self.backend.write(json.dumps(self.tweets))

    def find_hashtags(self, message):
        return [m.lower() for m in re.findall("#(\w+)", message)]

    def get_all_hashtags(self):
        hashtags = []
        for message in self.tweets:
            hashtags.extend(message["hashtags"])
        if hashtags:
            return set(hashtags)
        return "No hashtags found"
