import re
ans = input("What string?")

if t := re.search(r"^(([1-9]|10|11|12):?(?:[0-5][0-9])? (?:AM|PM))$" ,ans):
    print(t.group(1))
    print(t.group(2))


