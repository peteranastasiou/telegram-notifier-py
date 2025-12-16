from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

class Message(BaseModel):
  message: str
  channel: str

app = FastAPI()
tag = "Telegram Notifier"

@app.get("/", tags=[tag], response_class=HTMLResponse)
def service_info():
  return """
    <html>
      <body>
        <h1>Telegram Notifier</h1>
        <p>A service for forwarding messages to telegram bot</p>
        <p><a href="/docs">Swagger</a></p>
      </body>
    </html>
    """

@app.post("/message/", tags=[tag])
def post_message(msg: Message):
  print(msg)
  return msg
