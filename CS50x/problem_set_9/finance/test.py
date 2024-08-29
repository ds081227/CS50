from cs50 import SQL

db = SQL("sqlite:///finance.db")

user_id = 3
symbol = "A"

records = db.execute(
        "SELECT stock_symbol, SUM(CASE WHEN transaction_type = 'buy' THEN shares "
        "WHEN transaction_type = 'sell' THEN -shares "
        "ELSE 0 END) as total_shares "
        "FROM record WHERE user_id = ? AND stock_symbol = ? GROUP BY stock_symbol", user_id, symbol
        )

print(records)
