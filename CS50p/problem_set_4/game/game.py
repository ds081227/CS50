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

