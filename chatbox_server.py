from flask import Flask, redirect, render_template, request, url_for

from chatbox_userdata import fill_info

# import sqlite3

# signup_menu = "chatbox_signup.html"t
# signin_menu = "chatbox_signin.html"

app = Flask(__name__)
app.config["SECRET_KEY"] = "14885269yateshakalitkurazebu"


def user_info():
    user_info = {"username": "", "password": "", "email": ""}
    if request.method == "POST":
        user_info = {
            "username": request.form.get("username1"),
            "password": request.form.get("password1"),
            "email": request.form.get("email1"),
        }
        fill_info(user_info["username"], user_info["email"], user_info["password"])
        return redirect(url_for("mainblog"))


def log_in():
    if request.method == "POST":
        return redirect(url_for("mainblog"))


def get_post_blog():
    if request.method == "POST":
        user_post_text = request.form.get("blog1")
        user_post_file = request.form.get("file1")
    return redirect(url_for("mainblog"))       

def main_page():
    return render_template("chatbox_main.html")


def signup():
    return render_template("chatbox_signup.html"), user_info()


def signin():
    return render_template("chatbox_signin.html"), log_in()


def main_blog():
    return render_template("chatbox_mainblog.html"), get_post_blog()


# app.route("/")
# app.route("/save_data", methods=["POST"])

app.add_url_rule("/", "main_page", main_page)
app.add_url_rule("/signup", "signup", signup, methods=["post", "get"])
app.add_url_rule("/signin", "signin", signin, methods=["post", "get"])
app.add_url_rule("/main_blog", "mainblog", main_blog, methods=["post", "get"])


if __name__ == "__main__":
    app.run(host=("0.0.0.0"), debug=True)
