from cs50 import get_int


def main():
    card_number = get_int("Input: ")
    print(valid_check(card_number))


def valid_check(card_number):
    # Find the card_length
    card_length = int(len(str(card_number)))

    # Get the first two digit
    first_two = int((str(card_number)[:2]))

    sum_of_digit = 0
    # Loop until the all the numbers of the card has been read
    while card_number > 0:
        # Get the last digit and add to sum
        sum_of_digit += card_number % 10
        card_number = card_number // 10
        # Get the second last digit and add to sum
        temp_digit = card_number % 10 * 2

        if temp_digit >= 10:
            sum_of_digit += int(str(temp_digit)[0])
            sum_of_digit += int(str(temp_digit)[1])
        else:
            sum_of_digit += temp_digit

        card_number = card_number // 10

    # Start the checking
    if sum_of_digit % 10 == 0 and card_length <= 16:

        # AMEX
        if (first_two == 34 or first_two == 37) and card_length == 15:
            return "AMEX"

        # MASTERCARD
        if 55 >= first_two >= 51 and card_length == 16:
            return "MASTERCARD"

        # VISA
        if 49 >= first_two >= 40 and (card_length == 13 or card_length == 16):
            return "VISA"

        else:
            return "INVALID"

    else:
        return "INVALID"


main()
