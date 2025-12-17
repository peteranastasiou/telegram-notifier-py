from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import requests
import os

# Data models
class Message(BaseModel):
  message: str

# Pushover keys
pushover_apikey = os.environ["PUSHOVER_APIKEY"]
pushover_userkey = os.environ["PUSHOVER_USERKEY"]

# Initialise Webservice
app = FastAPI()
tag = "Pushover Notifier"

@app.get("/", tags=[tag], response_class=HTMLResponse)
def service_info():
  return """
    <html>
      <body>
        <h1>Pushover Notifier</h1>
        <p>A service for forwarding messages to Pushover</p>
        <p><a href="/docs">Swagger</a></p>
      </body>
    </html>
    """

@app.post("/message/", tags=[tag])
def post_message(msg: str):
  # Make a post to pushover
  # conn = http.client.HTTPSConnection("api.pushover.net:443")
  # conn.request("POST", "/1/messages.json",
  #   urllib.parse.urlencode({
  #     "token": pushover_apikey,
  #     "message": "hello world",
  #   }), { "Content-type": "application/x-www-form-urlencoded" })
  # return conn.getresponse()

  requests.post("https://api.pushover.net/1/messages.json", data={
    "token": pushover_apikey,
    "user": pushover_userkey,
    "message": msg
  })

  return "OK"
