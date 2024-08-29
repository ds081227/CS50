from flask import redirect, render_template, session
from functools import wraps
import re
from random import randint

def apology(message, code=400):
    """Render message as an apology to user."""

    return render_template("apology.html", error_message = message, code = code)


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


def password_validation(password):
    flag = 0
    while True:
        if (len(password) < 8):
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        else:
            flag = 0
            break
    if flag == -1:
        return False
    return True


def name_mask(name):
    masked_name = []
    name_list = name.split()
    for name in name_list:
        limit = round(len(name) / 2)
        for i in range(limit):
            masked_name.append(name[i])
        for i in range(limit, len(name)):
            masked_name.append("*")
        masked_name.append(" ")
    return(''.join(masked_name))

def account_number_generator():
    return randint(10000000,99999999)





