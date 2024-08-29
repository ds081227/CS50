while True:
    try:
        while True:
            x,y = input("Fraction: ").split("/")
            if int(x)/int(y) <= 1:
                break
        fuel = round((int(x) /int(y)) * 100)
        if fuel >= 99:
                print("F")
        elif fuel <= 1:
                print("E")
        else:
            print(f"{fuel}%")
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break


