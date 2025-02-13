import logging

from flask import Flask, redirect, render_template, request, url_for

from chatbox_userdata import fill_info, check_info

from chatbox_blogs import fill_blogs

logging.basicConfig(level=logging.DEBUG)

# import sqlite3

# signup_menu = "chatbox_signup.html"t
# signin_menu = "chatbox_signin.html"

app = Flask(__name__)
app.config["SECRET_KEY"] = "14885269yateshakalitkurazebu"


# def user_info():
#     user_info = {"username": "", "password": "", "email": ""}
#     if request.method == "POST":
#         user_info = {
#             "username": request.form.get("username1"),
#             "password": request.form.get("password1"),
#             "email": request.form.get("email1"),
#         }
#         fill_info(user_info["username"], user_info["email"], user_info["password"])
#         return redirect(url_for("mainblog"))


# def log_in():
#     if request.method == "POST":
#         return redirect(url_for("mainblog"))


def main_page():
    return render_template("chatbox_main.html")


def signup():
    if request.method == "POST":
        if request.form.get("confirm_password1") != request.form.get("password1"):
            return render_template("chatbox_signup.html")
        else:
            fill_info(
            request.form.get("username1"), request.form.get("email1"), request.form.get("password1")
                )
            return redirect(url_for("mainblog"))
    else:
        return render_template("chatbox_signup.html")


def signin():
    if request.method == "POST":
        check_info(request.form.get("email2"), request.form.get("password2"))
    else:
        return render_template("chatbox_signin.html")


def main_blog():
    if request.method == "POST":
        user_post_file = request.form.get("file1")
        fill_blogs(request.form.get("blog1"))
        return render_template("chatbox_mainblog.html")
    return render_template("chatbox_mainblog.html")


def friends_page():
    return render_template('friend-page.html')

# app.route("/")
# app.route("/save_data", methods=["POST"])

app.add_url_rule("/", "main_page", main_page)
app.add_url_rule("/signup", "signup", signup, methods=["post", "get"])
app.add_url_rule("/signin", "signin", signin, methods=["post", "get"])
app.add_url_rule("/main_blog", "mainblog", main_blog, methods=["post", "get"])
app.add_url_rule("/friends_page", "friends_page", friends_page)

if __name__ == "__main__":
    app.run(host=("0.0.0.0"), debug=True)
