import sys
import requests
import json

if len(sys.argv) == 2:
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Not a number")
else:
    sys.exit("Missing command-line or command line is not a number.")

info = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
USD = info.json()
rate = USD["bpi"]["USD"]["rate"].replace(",", "")
rate = float(rate)

price = rate * amount

print(f"${price:,.4f}")