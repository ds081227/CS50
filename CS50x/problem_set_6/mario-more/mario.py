from cs50 import get_int

while True:
    n = get_int("Height: ")
    if 0 < n < 9:
        break

for i in range(1, n + 1):
    print(" " * (n - i) + "#" * i + "  " + "#" * i)
