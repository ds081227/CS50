try:
    x = int(input("What's x?"))
    print("x is",(x))
    print(f"x is {x}")
except ValueError:
    print("x is not an interger")
