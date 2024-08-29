from validator_collection import validators, checkers

try:
    user_input = input("Email: ")
    email_address = checkers.is_email(user_input)
    print(email_address)
except ValueError:
    print("wrong input")
