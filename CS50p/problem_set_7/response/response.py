from validator_collection import checkers

def main():
    print(validate(input("What's your email address? ")))

def validate(s):
    if checkers.is_email(s):
        return str("Valid")
    else:
        return str("Invalid")


if __name__ == "__main__":
    main()
