from flask import Flask, render_template, request

from chatbox_userdata import fill_info

# import sqlite3

# signup_menu = "chatbox_signup.html"t
# signin_menu = "chatbox_signin.html"

app = Flask(__name__)
app.config["SECRET_KEY"] = "14885269yateshakalitkurazebu"

def user_info():
    user_info = {"username": "", "password": "", "email": ""}
    if request.method == "POST":
        user_info = {"username": request.form.get("username1"), "password": request.form.get("password1"), "email": request.form.get("email1")}
        fill_info(user_info["username"], user_info["email"], user_info["password"])
        return main_page()
    
def main_page():
    return render_template("chatbox_main.html")


def signup():
    return render_template("chatbox_signup.html"), user_info()
    

def signin():
    return render_template("chatbox_signin.html")


# app.route("/")
# app.route("/save_data", methods=["POST"])

app.add_url_rule("/", "main_page", main_page)
app.add_url_rule("/signup", "signup", signup)
app.add_url_rule("/signin", "signin", signin)


if __name__ == "__main__":
    app.run(host=("0.0.0.0"), debug=True)
