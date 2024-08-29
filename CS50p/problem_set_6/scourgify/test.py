import sys
import csv
from tabulate import tabulate
with open(sys.argv[1]) as file:
    students = []
    reader = csv.DictReader(file)
    for row in reader:
        if "name" in row and "house" in row:
            print("True")
            break
        else:
            print("wrong file")
            break

if sys.argv[1] == "before.csv" or sys.argv[1] == "before_long.csv" and sys.argv[2].endswith(".csv")
