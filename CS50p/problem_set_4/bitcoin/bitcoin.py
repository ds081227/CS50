import requests
import sys
import json

def float_check(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) == 2 and float_check(sys.argv[1]):
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r = response.json()
    rate = r.get("bpi").get("USD").get("rate")
    x,y = rate.split(".")
    x = float(x.replace(",",""))
    y = float(int(y)/10000)
    converted_rate = float(x + y)
    amount = converted_rate * float(sys.argv[1])
    print(f"${amount:,.4f}")

else:
    sys.exit("Command-line argument is not a number")
