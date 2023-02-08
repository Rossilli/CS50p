def main():
    fuel = get_input()


def get_input():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = [int(i) for i in fraction.split("/")]
            if x > y or y == 0:
                raise ValueError
            percentage = int((x / y) * 100)
            if percentage <=1:
                print("E")
                break
            elif percentage >= 99:
                print("F")
                break
            else:
                print(f"{percentage}%")
                break


        except (ValueError, ZeroDivisionError):
            continue



main()