"""free.churchless.tech AI agent"""
import json
import requests
from .base_agent import BaseAIAgent
from typings import AIRequestMessage # pylint: disable=import-error


# pylint: disable-next=too-few-public-methods
class FreeChurchlessAgent(BaseAIAgent):
    """free.churchless.tech AI agent"""
    def __init__(
        self,
        endpoint: str = "https://free.churchless.tech/v1/chat/completions",
        token: str | None = None,
        premessages: list[AIRequestMessage] | None = None,
    ) -> None: # pylint: disable=useless-parent-delegation
        """
        Returns the instance of FreeChurchless Agent class.
        Parameters:
                endpoint (str): URL with API endpoint
                token (str | None): No need for this API
                premessages (list[AIRequestMessage] | None): list of messages that
                        will be sent with each request (used for system prompts)
        Returns:
                FreeChurchlessAgent class instance
        """
        super().__init__(endpoint, token, premessages)

    def use(self, messages: list[AIRequestMessage]) -> list[str]:
        """
        Send a request to AI Agent
        Parameters:
                messages (list[AIRequestMessage]): list of messages
        Returns:
                hints (list[str]): list of text hints
        """
        result = requests.post(
            self.endpoint,
            json={"model": "gpt-3.5-turbo", "messages": self.premsg + messages},
            timeout=30,
        )
        try:
            return json.loads(
                result.json()["choices"][0]["message"]["content"]
            ).get("hints", [])
        except Exception: # pylint: disable=broad-exception-caught
            return []
