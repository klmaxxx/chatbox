import codecs

a = codecs.open("chatbox_signup.html", "r", "utf-8")
signupmenu = a.read()

b = codecs.open("chatbox_main.html", "r", "utf-8")
main_page_html = b.read

print(signupmenu)


def show_password1():
    if '<input type="radio" name="showpassword1 value="Show password>"':
            return '<input type="text" name = "password1 placeholder="Password">'
