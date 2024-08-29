import random
def main():
    level = get_level()
    user_attempt = 0
    user_score = 0
    while 10 > user_attempt:
        number_list = generate_integer(level)
        if calculation(number_list) == True:
            user_score += 1
        user_attempt = user_attempt + 1
    print("Your score is:",user_score)

def get_level():
    while True:
        try:
            user_level = int(input("Level: "))
            if 1 <= int(user_level) <= 3:
                return user_level
        except ValueError:
            continue

def generate_integer(level):
    num_needed = 2
    numbers = []
    while num_needed > 0:
        if level == 1:
            numbers.append(random.randint(0, 9))
        elif level == 2:
            numbers.append(random.randint(10, 99))
        elif level == 3:
            numbers.append(random.randint(100, 999))
        num_needed -= 1
    return numbers

def calculation(list):
    answer = list[0] + list[1]
    user_attempt = 3
    while user_attempt > 0:
        try:
            print(f"{list[0]} + {list[1]} = ",end = "")
            user_answer = int(input())
            if user_answer == answer:
                return True
            elif user_answer != answer:
                print("EEE")
                user_attempt = user_attempt -1
        except ValueError:
            print("EEE")
            user_attempt = user_attempt -1
    if user_attempt == 0:
        print(f"{list[0]} + {list[1]} = {answer}")


if __name__ == "__main__":
    main()


