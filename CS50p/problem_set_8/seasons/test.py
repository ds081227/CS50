from datetime import date
import sys
import inflect

year,month,day = input("Date of Birth: ").split("-")

input_date = date(int(year), int(month), int(day))
today = date.today()


result = input_date - today
print(result)


