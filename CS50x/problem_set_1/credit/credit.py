import sys

def main():
    card_number = (input("Card Number: "))
    print(calculate(card_number))





def calculate(number):
    every_other_digit = 0
    for i in str(number)[::2]:
        temp = int(i) * 2
        for i in str(temp):
            every_other_digit += int(i)
    not_multiplied_number = 0
    for i in str(number)[1::2]:
        not_multiplied_number += int(i)
    total = every_other_digit + not_multiplied_number
    print(total)
    if total % 10 == 0:
        if len(number) == 15 and number.startswith(("34","37")):
            return ("AMEX")
        elif len(number) == 16 and number.startswith(("51","52","53","54","55")):
            return ("MASTERCARD")
        elif len(number) == 13 or len(number) == 16 and number.startswith("4"):
            return("VISA")
    else:
        return str("Invalid")


def check(n):
    if n % 10 == 0:
        return True
    else:
        return str("Invalid")
main()
