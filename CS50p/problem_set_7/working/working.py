import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if t := re.search(r"^(([1-9]|10|11|12):?([0-5][0-9])? (?:AM|PM)) to (([1-9]|10|11|12):?([0-5][0-9])? (?:AM|PM))$",s):
        if "PM" in t.group(1):
            if int(t.group(2)) == 12:
                hour_1 = 12
            else:
                hour_1 = int(t.group(2)) + 12
            if t.group(3) == None:
                minute_1 = 0
            else:
                minute_1 = int(t.group(3))
        elif "AM" in t.group(1):
            if int(t.group(2)) == 12:
                hour_1 = 0
            else:
                hour_1 = int(t.group(2))
            if t.group(3) == None:
                minute_1 = 0
            else:
                minute_1 = int(t.group(3))
        if "PM" in t.group(4):
            if int(t.group(5)) == 12:
                hour_2 = 12
            else:
                hour_2 = int(t.group(5)) + 12
            if t.group(6) == None:
                minute_2 = 0
            else:
                minute_2 = int(t.group(6))
        elif "AM" in t.group(4):
            if int(t.group(5)) == 12:
                hour_2 = 0
            else:
                hour_2 = int(t.group(5))
            if t.group(6) == None:
                minute_2 = 0
            else:
                minute_2 = int(t.group(6))
        return str(f"{hour_1:02}:{minute_1:02} to {hour_2:02}:{minute_2:02}")
    else:
        raise ValueError("Wrong input")

if __name__ == "__main__":
    main()
