"""OpenAI agent"""
import json
import requests
from .base_agent import BaseAIAgent
from typings import AIRequestMessage # pylint: disable=import-error


# pylint: disable-next=too-few-public-methods
class OpenAIAgent(BaseAIAgent):
    """OpenAI agent"""
    def __init__(
        self,
        endpoint: str = "https://api.openai.com/v1/chat/completions",
        token: str | None = None,
        premessages: list[AIRequestMessage] | None = None,
    ) -> None: # pylint: disable=useless-parent-delegation
        """
        Returns the instance of OpenAI Agent class.
        Parameters:
                endpoint (str): URL with API endpoint
                token (str | None): Token for OpenAI API
                premessages (list[AIRequestMessage] | None): list of messages that
                        will be sent with each request (used for system prompts)
        Returns:
                OpenAIAgent class instance
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
            headers={"Authorization": "Bearer " + self.token},
        )
        try:
            return json.loads(
                result.json()["choices"][0]["message"]["content"]
            ).get("hints", [])
        except Exception: # pylint: disable=broad-exception-caught
            return []
