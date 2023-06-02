"""Main"""
from fastapi import FastAPI
from agents import OpenAIAgent
from typings import Message


tokens = {}


app = FastAPI()

TOKEN = open("token.txt", encoding="utf-8").read().strip()
PROMPT = open("prompt.txt", encoding="utf-8").read().strip()
agent = OpenAIAgent(token=TOKEN, premessages=[{"role": "system", "message": PROMPT}])


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
