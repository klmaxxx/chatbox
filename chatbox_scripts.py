import codecs

a = codecs.open("chatbox_signup.html", "r", "utf-8")
signupmenu = a.read()

print(signupmenu)


def show_password1():
    return signupmenu
    if '<input type="radio" name="showpassword1 value="Show password>"':
        return '<input type="text" name = "password1 placeholder="Password">'
