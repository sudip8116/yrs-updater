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
    print("server pull by pythonanywhere")
    return "server pulled"


def request_update():
    while True:
        try:
            res = rq.get(main_site_url, headers=headers)
            print(f"{res.status_code} : {res.text}")
        except:
            print("server down")
        sleep(1)


def request_update_thread():
    Thread(target=request_update).start()


request_update_thread()

