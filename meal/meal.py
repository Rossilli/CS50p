def main():
    time = input("What time is it? ")
    food = convert(time)
    if food >= 7 and food <= 8:
        print("breakfast time")
    elif food >= 12 and food <= 13:
        print("lunch time")
    elif food >= 18 and food <= 19:
        print("dinner time")


def convert(time):
    hour, min = time.split(":")
    hour = float(hour) + (float(min) / 60)
    return hour


if __name__ == "__main__":
    main()