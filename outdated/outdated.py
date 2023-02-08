import re

def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        try:
            date = input("Date: ").title()
            if "/" in date:
                month, day, year = date.split("/")
            elif "," in date:
                date = date.replace(",", " ")
                month, day, year = date.split()
                if month in months:
                    month = months.index(month) + 1
            else:
                continue
            if int(month) <= 12 and int(month) >= 1 and int(day)  >= 0 and int(day) <= 31:
                break
        except ValueError:
            continue

    print(f"{int(year)}-{int(month):02}-{int(day):02}")

main()