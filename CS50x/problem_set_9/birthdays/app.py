import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        name = request.form.get("name")
        if not name:
            return redirect("/")

        month = request.form.get("month")
        if not month or month.isdigit() == False:
            return redirect("/")

        day = request.form.get("day")
        if not day or day.isdigit() == False:
            return redirect("/")

        if not validation(int(month),int(day)):
            return redirect("/")

        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
        return redirect("/")

    else:
        # TODO: Display the entries in the database on index.html
        rows = db.execute("SELECT * FROM birthdays")
        print(rows)
        return render_template("index.html", birthdays = rows)

@app.route("/delete", methods=["POST"])
def delete_birthday():
    # Delete birthday
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM birthdays WHERE id = ?", id)
    return redirect("/")


@app.route("/edit", methods=["POST"])
def edit_birthday():
    id = request.form.get("id")
    if id:
        row = db.execute("SELECT * FROM birthdays WHERE id = ?", id)
    return render_template("edit.html", birthday = row[0])

@app.route("/update", methods=["POST"])
def update_birthday():
    id = request.form.get("id")
    name = request.form.get("name")
    if not name:
        return redirect("/")

    month = request.form.get("month")
    if not month or month.isdigit() == False:
        return redirect("/")

    day = request.form.get("day")
    if not day or day.isdigit() == False:
        return redirect("/")

    if not validation(int(month),int(day)):
        return redirect("/")

    db.execute("UPDATE birthdays SET name = ?, month = ?, day = ? WHERE id = ?", name, month, day, id)
    return redirect("/")



def validation(month, day):
    big_month = [1, 3, 5, 7, 8, 10, 12]
    small_month = [4, 6, 9, 11]
    if month in big_month:
        if 1 <= day <= 31:
            return True
    elif month in small_month:
        if 1 <= day <= 30:
            return True
    elif month == 2:
        if 1 <= day <= 29:
            return True
    return False




