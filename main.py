"""Main"""
from fastapi import FastAPI
from pydantic import BaseModel # pylint: disable=no-name-in-module
from ai import AIAgent


tokens = {}


app = FastAPI()

TOKEN = open("token.txt", encoding="utf-8").read()
agent = AIAgent("https://api.openai.com/v1/chat/completions", TOKEN)


# pylint: disable-next=missing-class-docstring, too-few-public-methods
class Message(BaseModel):
    from_name: str
    text: str


# pylint: disable-next=missing-function-docstring
def parse_messages_to_prompt(messages: list[Message]) -> list[str]:
    return [{
                "role": "user",
                "content": f"({message.from_name}): {message.text}"
            } for message in messages]


@app.post("/predict")
# pylint: disable-next=missing-function-docstring
async def predict(messages: list[Message]):
    response = agent.use(parse_messages_to_prompt(messages))
    return response
