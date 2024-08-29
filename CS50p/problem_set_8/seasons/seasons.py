from datetime import date
import sys
import inflect


def main():
        print(convert(input("Date of Birth: ")))

def convert(user_input):
    try:
        year,month,day = user_input.split("-")
        result = date.today() - date(int(year), int(month), int(day))
        return str(f"{inflect.engine().number_to_words(result.days * 24 * 60, andword = "")} minutes".capitalize())
    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
