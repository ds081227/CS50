import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import apology, login_required, lookup, usd


# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    user = db.execute("SELECT username, cash FROM users WHERE id = ?", user_id)
    user[0]["grand_total"] = user[0]["cash"]

    records = db.execute(
        "SELECT stock_symbol, SUM(CASE WHEN transaction_type = 'buy' THEN shares "
        "WHEN transaction_type = 'sell' THEN -shares "
        "ELSE 0 END) as total_shares "
        "FROM record WHERE user_id = ? GROUP BY stock_symbol", user_id
    )

    for record in records:
        record["current_price"] = lookup(record["stock_symbol"])["price"]
        record["total_value"] = record["current_price"] * record["total_shares"]
        user[0]["grand_total"] += record["total_value"]

    return render_template("index.html", records=records, user=user[0])


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # Get the info for database insertion
        user_id = session["user_id"]
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        stock_data = lookup(symbol)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        def is_fractional(n):
            return n != int(n)

        # Check for blank fill in, shares non-negative, symbol doesn't exist
        if not symbol or not shares or stock_data == None or not shares.isdigit() or int(shares) < 0 or is_fractional(float(shares)):
            return apology("Incorrect input for stock symbol or shares", 400)

        # Check whether user has enough money to buy the stock
        amount_needed = stock_data["price"] * int(shares)
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        if amount_needed > user_cash:
            return apology("Not enough cash", 400)

        # Insert buy record into database
        db.execute(
            "INSERT INTO record (user_id, stock_symbol, shares, price, purchase_time, transaction_type) "
            "VALUES(?, ?, ?, ?, ?, ?)",
            user_id, symbol, shares, stock_data["price"], timestamp, "buy"
        )

        # Update the cash in user table
        db.execute(
            "UPDATE users SET cash = ? "
            "WHERE id = ?",
            user_cash - amount_needed, user_id
        )
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    records = db.execute("SELECT * FROM record WHERE user_id = ?", user_id)
    return render_template("history.html", records=records)


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        user_id = session["user_id"]
        cash = request.form.get("cash")
        if not cash or not cash.isdigit() or int(cash) < 0:
            return apology("Invalid input of cash", 400)

        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        # Update the cash in user table
        db.execute(
            "UPDATE users SET cash = ? "
            "WHERE id = ?",
            user_cash + float(cash), user_id
        )
        return redirect("/")
    else:
        return render_template("add.html")


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


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        # Check if field is blank and symbol exist in database
        if not symbol or lookup(symbol) == None:
            return apology("Stock symbol doesn't exist.", 400)

        # Retrieve the stock info and render info to html
        stock_data = lookup(symbol)
        return render_template("quoted.html", symbol=stock_data["symbol"], price=usd(stock_data["price"]))
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        # Check if any field is blank
        if not username or not password or not confirmation:
            return apology("Username or password cannot be blank", 400)
        # Check if password equals to confirmation
        if password != confirmation:
            return apology("Password and confirmation doesn't match", 400)
        user_list = db.execute("SELECT username FROM users")
        # Check if user already exist in username list
        for user in user_list:
            if user["username"] == username:
                return apology("Username already exist", 400)

        # Add the user to the database
        hash = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES(? ,?)", username, hash)

        # Log user in and redirect to homepage
        user_id = db.execute("SELECT id FROM users WHERE username = ?", username)
        session["user_id"] = user_id[0]["id"]
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
       # Get the required data
        user_id = session["user_id"]
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        records = db.execute(
            "SELECT stock_symbol, SUM(CASE WHEN transaction_type = 'buy' THEN shares "
            "WHEN transaction_type = 'sell' THEN -shares "
            "ELSE 0 END) as total_shares "
            "FROM record WHERE user_id = ? AND stock_symbol = ? GROUP BY stock_symbol", user_id, symbol
        )
        stock_data = lookup(symbol)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Check for valid input
        if not symbol or not shares or int(shares) < 0 or stock_data == None:
            return apology("Invalid input of symbol or shares", 400)

        # Check whether user has enough shares to sell
        if records[0]["total_shares"] < int(shares):
            return apology("Not enough shares to sell", 400)

        # Insert buy record into database
        db.execute(
            "INSERT INTO record (user_id, stock_symbol, shares, price, purchase_time, transaction_type) "
            "VALUES(?, ?, ?, ?, ?, ?)",
            user_id, symbol, shares, stock_data["price"], timestamp, "sell"
        )

        # Update the cash value in user database
        user_cash = int(db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"])
        user_cash += int(shares) * stock_data["price"]
        db.execute(
            "UPDATE users SET cash = ? "
            "WHERE id = ?",
            user_cash, user_id
        )
        return redirect("/")

    else:
        user_id = session["user_id"]
        records = db.execute(
            "SELECT stock_symbol, SUM(shares) AS total_shares FROM record WHERE user_id = ? GROUP BY stock_symbol", user_id)
        return render_template("sell.html", records=records)
