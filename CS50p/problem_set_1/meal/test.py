def main():
    input_time = input("What time is it? ")
    if "p.m." or "pm" in input_time:
        converted_time = convert(input_time.split()[0])
        if converted_time < 12:
            converted_time = converted_time + 12
        meal_check(converted_time)
    elif "a.m." or "am" in input_time:
        converted_time = convert(input_time.split()[0])
        meal_check(converted_time)
    else:
        converted_time = convert(input_time)
        meal_check(converted_time)

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60

def meal_check(converted_time):
    if 8 >= converted_time >= 7:
        print("breakfast time")
    elif 13 >= converted_time >= 12:
        print("lunch time")
    elif 19 >= converted_time >= 18:
        print("dinner time")
    else:
        print("Not eating")

if __name__ == "__main__":
    main()



def main():
    input_time = input("What time is it? ")
    converted_time = convert(input_time)
    if 8 >= converted_time >= 7:
        print("breakfast time")
    elif 13 >= converted_time >= 12:
        print("lunch time")
    elif 19 >= converted_time >= 18:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return float(minutes) / 60 + float(hours)


if __name__ == "__main__":
    main()
