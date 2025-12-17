from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests
import os
import threading
import queue

# Pushover keys
pushover_apikey = os.environ["PUSHOVER_APIKEY"]
pushover_userkey = os.environ["PUSHOVER_USERKEY"]

# Initialise message queue
msg_queue = queue.Queue()

def send_messages():
  while True:
    msg = msg_queue.get()
    requests.post("https://api.pushover.net/1/messages.json", data={
      "token": pushover_apikey,
      "user": pushover_userkey,
      "message": msg
    })
    msg_queue.task_done()

msg_thread = threading.Thread(target=send_messages, daemon=True)
msg_thread.start()

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
  msg_queue.put(msg)
  return "OK"
