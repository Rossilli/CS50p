import sys
import os
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
        if os.path.isfile(sys.argv[1]):
            with open(sys.argv[1], "r") as file:
                prices = csv.DictReader(file)
                print(tabulate(prices, headers = "keys", tablefmt = "grid"))
        else:
            sys.exit("No file")
    else:
        sys.exit("Invalid")


if __name__ == "__main__":
    main()