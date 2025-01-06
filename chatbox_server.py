import os

from flask import Flask, redirect, request, url_for

from chatbox_userdata import fill_info

import sqlite3

# chatbox_main = "chatbox/chatbox_main.html"

folder = os.getcwd()

app = Flask(__name__, static_folder=folder)
app.config["SECRET_KEY"] = "14885269yateshakalitkurazebu"

def user_info():
    username = request.form["username1"]
    email = request.form["email1"]
    password = request.form["password1"]
    fill_info()

def main_page():
    return redirect(url_for("static", filename="chatbox_main.html"))

app.route("/")
app.route("/save_data", methods=["POST"])

app.add_url_rule("/main_page", "main_page", main_page)

if __name__ == "__main__":
    app.run()
    user_info()
