from fastapi import FastAPI
from pydantic import BaseModel

class Message(BaseModel):
  message: str
  channel: str

app = FastAPI()

@app.get("/")
def service_info():
  return "A service for forwarding messages to telegram bot"

@app.post("/message/")
def post_message(msg: Message):
  print(msg)
  return msg
