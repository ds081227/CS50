import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if m := re.search(r"src=\"https?://(?:www\.)?youtube\.com/embed/(.+?)\"",s):
        result = m.group(1)
        return str(f"https://youtu.be/{result}")
    else:
        return None
if __name__ == "__main__":
    main()
