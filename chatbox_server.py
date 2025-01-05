from flask import Flask, session, redirect, url_for

chatbox_main = "chatbox/chatbox_main.html"

def main_page():
    return chatbox_main

app = Flask(__name__)

if __name__ == "__main__":
    app.run()
