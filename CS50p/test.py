import random
while True:
    try:
        while True:
            game_level = int(input("Level: "))
            if game_level > 0:
                answer = random.randint(1, game_level)
                while True:
                    guess = input("Guess: ")
                    if guess.isdigit() and int(guess) > 0:
                        if int(guess) == answer:
                            print("Just right!")
                            break
                        elif int(guess) > answer:
                            print("Too large!")
                        elif int(guess) < answer:
                            print("Too small!")
                break
    except ValueError:
        pass
    else:
        break

def main():
    level = get_level()
    user_attempt = 0
    user_score = 0
    while 2 > user_attempt:
        generate_integer(level)
        number_list = generate_integer(level)
        calculation(number_list)
        user_attempt = user_attempt + 1
    user_score = calculation(number_list)
    print("Your score is:",user_score)

def main():
    level = get_level()
    user_attempt = 0
    while 2 > user_attempt:
        number_list = generate_integer(level)
        calculation(number_list)
        user_score = calculation(number_list)
        user_attempt = user_attempt + 1
    print("Your score is:",user_score)

elif len(sys.argv) == 2 and float_check(sys.argv[1]):
    user_bitcoin = int(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r = response.json()
    bpi = r.get("bpi")
    USD = bpi.get("USD")
    rate = USD.get("rate")
    x,y = rate.split(".")
    x = float(x.replace(",",""))
    y = float(int(y)/10000)
    converted_rate = float(x + y)
    print(rate)
    amount = converted_rate * user_bitcoin
    print(f"${amount:,.4f}")

    bpi = r.get("bpi")
    USD = bpi.get("USD")
    rate = USD.get("rate")
