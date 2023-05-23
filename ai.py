"""Module with AI staff"""
from typing import Literal
import json
import requests

# pylint: disable-next=missing-class-docstring, too-few-public-methods
class AIRequestMessage:
    role: Literal["system", "user"]
    content: str


# pylint: disable-next=missing-class-docstring
class AIAgent:
    def __init__(self, endpoint="https://free.churchless.tech/v1/chat/completions", token: str | None = None) -> None:
        self.endpoint = endpoint
        self.security = {
            "role": "system",
            "content": open("prompt.txt", encoding="utf-8").read()
        }
        self.token = token


    def use(self, messages: list[AIRequestMessage]) -> dict:
        """Generate response by messages"""
        print({
            "model": "gpt-3.5-turbo",
            "messages": [self.security] + messages
        })
        if self.token is None:
            result = requests.post(self.endpoint, json={
                "model": "gpt-3.5-turbo",
                "messages": [self.security] + messages
            }, timeout=30)
        else:
            result = requests.post(self.endpoint, json={
                "model": "gpt-3.5-turbo",
                "messages": [self.security] + messages
            }, timeout=30, headers={
                "Authorization": "Bearer " + self.token
            })
        print(result.json())
        try:
            return json.loads(result.json()["choices"][0]["message"]["content"])
        except Exception: # pylint: disable=broad-exception-caught
            return {"ok": False, "exception": result.text}
