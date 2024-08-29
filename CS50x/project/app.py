import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import apology, login_required, usd, password_validation, name_mask, account_number_generator


# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///bank.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Homepage
@app.route("/")
def index():
    return render_template("index.html")


# Homepage
@app.route("/homepage")
@login_required
def homepage():
    user_id = session["user_id"]
    user = db.execute("SELECT name, cash, account_number FROM users WHERE id = ?", user_id)
    records = db.execute("SELECT record.giver_id, record.receiver_id, record.amount, record.transaction_type, record.time, g.account_number AS giver_account, r.account_number AS receiver_account "
                        "FROM record "
                        "JOIN users g ON record.giver_id = g.id "
                        "JOIN users r ON record.receiver_id = r.id "
                        "WHERE g.id = ? OR r.id = ? "
                        "ORDER BY time" ,user_id, user_id)

    for record in records:
        if record["transaction_type"] == "transfer":
            if record["giver_id"] == user_id:
                record["transaction_type"] = "transfer out"
            else:
                record["transaction_type"] = "transfer in"

    return render_template("homepage.html", user = user[0], records = records)

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


# Deposit
@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    if request.method == "POST":
        user_id = session["user_id"]
        deposit = request.form.get("deposit")
        if not deposit or not deposit.isdigit() or int(deposit) < 0:
            return apology("Invalid input of deposit", 400)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        # Update the cash in user table
        db.execute(
            "UPDATE users SET cash = ? "
            "WHERE id = ?",
            user_cash + float(deposit), user_id
        )
        # Insert record into database
        db.execute(
            "INSERT into record(giver_id, receiver_id, amount, transaction_type, time) "
            "VALUES(?, ?, ?, ?, ?)",
            user_id, user_id, deposit, "deposit", timestamp
        )
        return redirect("homepage")
    else:
        return render_template("deposit.html")

# Withdraw
@app.route("/withdraw", methods=["GET", "POST"])
@login_required
def withdraw():
    if request.method == "POST":
        user_id = session["user_id"]
        withdraw = request.form.get("withdraw")
        if not withdraw or not withdraw.isdigit() or int(withdraw) < 0:
            return apology("Invalid input of withdrawal", 400)

        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if float(withdraw) > user_cash:
            return apology("Not enough cash to withdraw", 400)
        # Update the cash in user table
        db.execute(
            "UPDATE users SET cash = ? "
            "WHERE id = ?",
            user_cash - float(withdraw), user_id
        )

        # Insert record into database
        db.execute(
            "INSERT into record(giver_id, receiver_id, amount, transaction_type, time) "
            "VALUES(?, ?, ?, ?, ?)",
            user_id, user_id, withdraw, "withdraw", timestamp
        )

        return redirect("homepage")
    else:
        user_id = session["user_id"]
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        return render_template("withdraw.html", user_cash = user_cash)


# Transfer
@app.route("/transfer", methods=["GET", "POST"])
@login_required
def transfer():
    if request.method == "POST":
        user_id = session["user_id"]
        transfer_amount = request.form.get("transfer_amount")
        target_account = request.form.get("target_account")
        user = db.execute("SELECT * FROM users WHERE id = ?", user_id)

        # Input check
        if not transfer_amount or not target_account or float(transfer_amount) < 0:
            return apology("Invalid input of account or amount", 400)
        target_info = db.execute("SELECT * FROM users WHERE account_number = ?", target_account)
        if not target_info:
            return apology("Transferee account does not exist", 400)
        if user[0]["cash"] < float(transfer_amount):
            return apology("Not enough cash for transfer", 400)
        if user[0]["id"] == target_info[0]["id"]:
            return apology("Cannot transfer to your own account", 400)
        return render_template("transfer_confirm.html",
                               target_name = name_mask(target_info[0]["name"]),
                               account_number = target_info[0]["account_number"],
                               transfer_amount = transfer_amount
                               )
    else:
        return render_template("transfer.html")


@app.route("/confirmation", methods=["POST"])
def confirmation():
    user_id = session["user_id"]
    transfer_amount = request.form.get("transfer_amount")
    target_account = request.form.get("target_account")
    user = db.execute("SELECT * FROM users WHERE id = ?", user_id)

    # Input check
    if not transfer_amount or not target_account or float(transfer_amount) < 0:
        return apology("Invalid input of account or amount", 400)
    target_info = db.execute("SELECT * FROM users WHERE account_number = ?", target_account)
    if not target_info:
        return apology("Transferee account does not exist", 400)
    if user[0]["cash"] < float(transfer_amount):
        return apology("Not enough cash for transfer", 400)

    # Transfer the cash
    db.execute("UPDATE users SET cash = ? WHERE id = ?", user[0]["cash"] - float(transfer_amount), user_id)
    db.execute("UPDATE users SET cash = ? WHERE account_number = ?", target_info[0]["cash"] + float(transfer_amount), target_account)

    # Insert record into database
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.execute(
            "INSERT into record(giver_id, receiver_id, amount, transaction_type, time) "
            "VALUES(?, ?, ?, ?, ?)",
            user_id, target_info[0]["id"], transfer_amount, "transfer", timestamp
        )

    return redirect("/homepage")



@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        # Check if any field is blank
        if not name or not username or not password or not confirmation:
            return apology("Name, username or password cannot be blank", 400)

        # Check if password equals to confirmation
        if password != confirmation:
            return apology("Password and confirmation doesn't match", 400)

        # Check if password is valid
        if not password_validation(password):
            return apology("Password does not meet requirement", 400)

        # Check if user already exist in username list
        user_list = db.execute("SELECT username FROM users")
        for user in user_list:
            if user["username"] == username:
                return apology("Username already exist", 400)

        # Add the user to the database(name, username, password, generate bank account)
        hash = generate_password_hash(password)
        account_list = db.execute("SELECT account_number FROM users")
        account_numbers = [account['account_number'] for account in account_list]
        while True:
            account_number = account_number_generator()
            if account_number not in account_numbers:
                break
        db.execute("INSERT INTO users (name, username, hash, account_number) VALUES(?, ? ,?, ?)",name, username, hash, account_number)
        # Log user in and redirect to homepage
        user_id = db.execute("SELECT id FROM users WHERE username = ?", username)
        session["user_id"] = user_id[0]["id"]
        return redirect("/homepage")
    else:
        return render_template("register.html")


