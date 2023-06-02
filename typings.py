"""Module for advanced typing support"""
from typing import Literal
from pydantic import BaseModel # pylint: disable=no-name-in-module


# pylint: disable-next=missing-class-docstring, too-few-public-methods
class AIRequestMessage:
    role: Literal["system", "user"]
    content: str


# pylint: disable-next=missing-class-docstring, too-few-public-methods
class Message(BaseModel):
    from_name: str
    text: str
