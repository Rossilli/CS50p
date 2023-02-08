from datetime import date
import inflect
import re
import sys

p = inflect.engine()
def main():
    user_date = input("Date of Birth: ")
    try:
        yr, mo, dy = check_birth(user_date)
    except:
        sys.exit("Wrong date")
    user_date2 = date(int(yr), int(mo), int(dy))
    today = date.today()
    diff = today - user_date2
    minutes = diff.days * 24 * 60
    song = p.number_to_words(minutes, andword="")
    print(f"{song.capitalize()} minutes")


def check_birth(user_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", user_date):
        yr, mo, dy = user_date.split("-")
        return yr, mo, dy


if __name__ == "__main__":
    main()
