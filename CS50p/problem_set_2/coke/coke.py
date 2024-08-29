amount_due = 50
while True:
    if amount_due <= 0:
        print("Change Owed:",abs(amount_due))
        break
    else:
        print("Amount Due:", amount_due)
        inserted_coins = int(input("Insert Coin:" ))
        if inserted_coins == 25:
            amount_due = amount_due - 25
        elif inserted_coins == 10:
            amount_due = amount_due - 10
        elif inserted_coins == 5:
            amount_due = amount_due - 5







