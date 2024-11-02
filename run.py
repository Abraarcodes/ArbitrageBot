import subprocess
from flask import Flask, render_template, request, redirect, url_for
import threading
from colorama import Style, init
import datetime
from exchange_config import *

app = Flask(__name__)
init()

process_thread = None  # Store the reference to the process thread


def run_script(mode, renew, balance, symbol, ex_list):
    global process_thread
    i = 0
    while True:
        if i >= 1 and p.returncode == 1:
            return "Error occurred during script execution."
        if mode == "fake-money":
            p = subprocess.run([how_do_you_usually_launch_python, "bot-fake-money.py", symbol, balance, renew, symbol, ex_list])
            with open("balance.txt") as f:
                balance = f.read()
        elif mode == "classic":
            p = subprocess.run([how_do_you_usually_launch_python, "bot-classic.py", symbol, balance, renew, symbol, ex_list])
            with open("balance.txt") as f:
                balance = f.read()
        elif mode == "delta-neutral":
            p = subprocess.run([how_do_you_usually_launch_python, "bot-delta-neutral.py", symbol, balance, renew, symbol, ex_list])
            with open("balance.txt") as f:
                balance = f.read()
        else:
            return "Mode input is incorrect."

        i += 1

@app.route("/", methods=["GET", "POST"])
def index():
    global process_thread

    if request.method == "POST":
        mode = request.form["mode"]
        renew = request.form["renew"]
        balance = request.form["balance"]
        symbol = request.form["symbol"]
        ex_list = request.form["ex_list"]
        with open("start_balance.txt", "w") as f:
            f.write(balance)

        with open("balance.txt", "w") as f:
            f.write(balance)

        process_thread = threading.Thread(target=run_script, args=(mode, renew, balance, symbol, ex_list))
        process_thread.start()
    return render_template("parameter.html")

if __name__ == "__main__":
    app.run(debug=True)
