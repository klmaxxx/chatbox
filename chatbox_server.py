from flask import Flask, sessions, url_for, redirect 
import os

# chatbox_main = "chatbox/chatbox_main.html"


def main_page():
    return redirect(url_for('static', filename="chatbox_main.html"))

folder = os.getcwd()

app = Flask(__name__, static_folder=folder)
app.config["SECRET_KEY"] = "14885269yateshakalitkurazebu"

app.add_url_rule("/", "main_page", main_page)

if __name__ == "__main__":
    app.run()
