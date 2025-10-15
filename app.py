import os
import sys
from threading import Thread
from time import sleep
from flask import Flask
import requests as rq

# -------------------------------------------------
# 🔧 Ensure print() shows immediately in Render logs
# -------------------------------------------------
sys.stdout.reconfigure(line_buffering=True)
os.environ['PYTHONUNBUFFERED'] = '1'

main_site_url = "https://yourradiostation.pythonanywhere.com/request-update"
headers = {"auth": "3f9a7b2c1d8e4f6a0b9c2d7e8f1a3b"}
app = Flask(__name__)

# -------------------------------------------------
# Flask routes
# -------------------------------------------------
@app.route("/")
def home():
    print("Home route accessed", flush=True)
    return "Welcome from Render!"

@app.route("/pull")
def pull():
    print("Pulled by PythonAnywhere", flush=True)
    return "server pulled"

# -------------------------------------------------
# Background thread
# -------------------------------------------------
def request_update():
    print("Background thread started", flush=True)
    while True:
        try:
            res = rq.get(main_site_url, headers=headers, timeout=10)
            print(f"→ {res.status_code} : {res.text}", flush=True)
        except Exception as e:
            print("⚠️  server down:", e, flush=True)
        sleep(30)  # ping every minute

def request_update_thread():
    Thread(target=request_update, daemon=True).start()

# -------------------------------------------------
# Entry point
# -------------------------------------------------
if __name__ == "__main__":
    print("Starting Flask app...", flush=True)
    request_update_thread()
    app.run(host="0.0.0.0", port=5000)
