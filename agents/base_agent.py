"""Base AI agent class"""
from typings import AIRequestMessage # pylint: disable=import-error


# pylint: disable-next=too-few-public-methods
class BaseAIAgent:
    """Base AI agent"""
    def __init__(
                self,
                endpoint: str = "https://free.churchless.tech/v1/chat/completions",
                token: str | None = None,
                premessages: list[AIRequestMessage] | None = None
        ) -> None:
        '''
        Returns the instance of the AI Agent class.
        Parameters:
                endpoint (str): URL with API endpoint
                token (str | None): Credentials for your AI Agent API
                premessages (list[AIRequestMessage] | None): list of messages that 
                        will be sent with each request (used for system prompts)
        Returns:
                BaseAIAgent class instance
        '''
        self.endpoint = endpoint
        self.premsg = premessages
        self.token = token


    def use(self, messages: list[AIRequestMessage]) -> list[str]:
        '''
        Send a request to AI Agent
        Parameters:
                messages (list[AIRequestMessage]): list of messages
        Returns:
                hints (list[str]): list of text hints
        '''
        # at this point you need to implement the logic to send a request to your AI Agent API
        # here you need to write an authorization using the secret passed in self.token
        # and also formatting the message list from the argument to the format of your API
        # process the response and return the list of text hints
        # return [] if the request was not successful
        raise NotImplementedError()
