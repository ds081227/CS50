import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if m := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip):
        if int(m.group(1)) < 256 and int(m.group(2)) < 256 and int(m.group(3)) < 256 and int(m.group(4)) < 256 :
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
