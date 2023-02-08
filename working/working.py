import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    match_str = re.search(r'(((1[0-2])|([0-9])):?([0-5][0-9])? (AM|PM)) to (((1[0-2])|([0-9])):?([0-5][0-9])? (AM|PM))', s, re.IGNORECASE)
    if not match_str:
        raise ValueError
    time1 = match_str.group(1)
    time2 = match_str.group(7)

    # convert time to 24-hour format
    match_time1 = re.search(r'((1[0-2]|[0-9]):?([0-5][0-9])? (AM|PM))', time1, re.IGNORECASE)
    if not match_time1:
        raise ValueError
    hour1 = int(match_time1.group(2))
    if match_time1.group(4).upper() == 'PM' and hour1 != 12:
        hour1 += 12
    elif match_time1.group(4).upper() == 'AM' and hour1 == 12:
        hour1 = 0
    minutes1 = match_time1.group(3) or "00"
    time1 = f"{hour1:02}:{minutes1}"


    match_time2 = re.search(r'((1[0-2]|[0-9]):?([0-5][0-9])? (AM|PM))', time2, re.IGNORECASE)
    if not match_time2:
        raise ValueError
    hour2 = int(match_time2.group(2))
    if match_time2.group(4).upper() == 'PM' and hour2 != 12:
        hour2 += 12
    elif match_time2.group(4).upper() == 'AM' and hour2 == 12:
        hour2 = 0
    minutes2 = match_time2.group(3) or "00"
    time2 = f"{hour2:02}:{minutes2}"

    return f"{time1} to {time2}"

if __name__ == "__main__":
    main()
