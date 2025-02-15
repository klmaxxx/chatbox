from flask import Flask, redirect, render_template, request, session, url_for

from chatbox_userdata import fill_info, fill_posts, get_posts, get_user, user_exists, valid_user

app = Flask(__name__)
app.config["SECRET_KEY"] = "14885269yateshakalitkurazebu"


def main_page():
    return render_template("chatbox_main.html", session=session)


def signup():
    if request.method == "GET":
        if "username" in session:
            return redirect(url_for("mainblog"))
        return render_template("chatbox_signup.html")
    else:
        if request.form.get("password_confirm") != request.form.get("password"):
            error = "Passwords must match!"
        elif user_exists(request.form.get("username"), request.form.get("email")):
            error = "User with such name and/or email exists!"
        else:
            fill_info(
                request.form.get("username"),
                request.form.get("email"),
                request.form.get("password"),
            )
            u_id, name, *_ = get_user(request.form.get("username"))
            session["user_id"] = u_id
            session["username"] = name
            session["page"] = 1
            return redirect(url_for("mainblog"))
        return render_template("chatbox_signup.html", error=error)


def signin():
    if request.method == "GET":
        if "username" in session:
            return redirect(url_for("mainblog"))
        return render_template("chatbox_signin.html")
    else:
        if not valid_user(request.form.get("username"), request.form.get("password")):
            error = "Invalid username and/or password!"
            return render_template("chatbox_signin.html", error=error)
        else:
            u_id, name, *_ = get_user(request.form.get("username"))
            session["user_id"] = u_id
            session["username"] = name
            session["page"] = 1
            return redirect(url_for("mainblog"))


def main_blog():
    if request.method == "POST" and "username" in session:
        error = ""
        posts = []
        if len((text := request.form.get("text")).strip()) <= 5:
            error = "Post text length must be greater than 5 symbols and not empty!"
        else:
            fill_posts(session["user_id"], text)
            posts = get_posts(10, session["page"])
        return render_template("chatbox_mainblog.html", error=error, posts=posts, session=session)
    else:
        posts = get_posts(10, session["page"])
        return render_template("chatbox_mainblog.html", error="", posts=posts, session=session)


def next_page():
    if "username" in session:
        session["page"] += 1
    return redirect(url_for("mainblog"))


def prev_page():
    if "username" in session:
        session["page"] -= 1
    return redirect(url_for("mainblog"))


def friends_page():
    return render_template("friend-page.html")


def logout():
    session.pop("username", None)
    return redirect(url_for("main_page"))


# app.route("/save_data", methods=["POST"])

app.add_url_rule("/", "main_page", main_page)
app.add_url_rule("/signup", "signup", signup, methods=["post", "get"])
app.add_url_rule("/signin", "signin", signin, methods=["post", "get"])
app.add_url_rule("/main_blog", "mainblog", main_blog, methods=["post", "get"])
app.add_url_rule("/next_page", "next_page", next_page)
app.add_url_rule("/prev_page", "prev_page", prev_page)
app.add_url_rule("/friends_page", "friends_page", friends_page)
app.add_url_rule("/logout", "logout", logout)


if __name__ == "__main__":
    app.run(host=("0.0.0.0"), debug=True)
