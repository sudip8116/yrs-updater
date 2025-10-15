from threading import Thread
from time import sleep
from flask import Flask
import requests as rq

main_site_url = "https://yourradiostation.pythonanywhere.com/request-update"
headers = {"auth": "3f9a7b2c1d8e4f6a0b9c2d7e8f1a3b"}
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome"

@app.route("/pull")
def pull():
    print("Pulled by PythonAnywhere")
    return "server pulled"

def request_update():
    while True:
        try:
            res = rq.get(main_site_url, headers=headers, timeout=10)
            print(f"{res.status_code} : {res.text}")
        except Exception as e:
            print("server down:", e)
        sleep(60)  # ping every 1 minute

def request_update_thread():
    Thread(target=request_update, daemon=True).start()

if __name__ == "__main__":
    request_update_thread()
    app.run(host="0.0.0.0", port=5000)
