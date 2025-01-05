from flask import Flask, sessions, url_for, redirect 

chatbox_main = "chatbox/chatbox_main.html"


def main_page():
    return '''<!DOCTYPE html>
    <html>
        <head>
            <title>chatbox</title>
        </head></html
        <body>
        <h1> chatbox </h1>
        </body>
    </html>
    '''


app = Flask(__name__)
app.config["SECRET_KEY"] = "14885269yateshakalitkurazebu"

app.add_url_rule("/chatbox", "main_page", main_page)

if __name__ == "__main__":
    app.run()
