from cs50 import get_float


def main():
    while True:
        dollars = get_float("Change owed: ")
        if dollars > 0:
            break

    cents = dollars * 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickles = cents // 5
    cents = cents % 5

    pennies = cents // 1
    cents = cents - pennies

    coins = int(quarters + dimes + nickles + pennies)

    print(coins)


main()
