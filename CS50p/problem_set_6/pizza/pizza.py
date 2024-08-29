import sys
import csv
from tabulate import tabulate
def main():
    print("abc")
if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 2:
    if sys.argv[1].endswith(".csv"):
        try:
            pizza_list = []
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for row in reader:
                    pizza_list.append({"pizza":row[0], "small":row[1], "large":row[2]})
            print(tabulate(pizza_list, headers = "firstrow", tablefmt = "grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
