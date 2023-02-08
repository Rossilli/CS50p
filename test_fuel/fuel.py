def main():
    fraction = input("Fraction: ")
    frac_conv = convert(fraction)
    output = gauge(frac_conv)
    print(output)


def convert(fraction):
    while True:
        try:
            numerator, denominator = fraction.split("/")
            new_numerator = int(numerator)
            new_denominator = int(denominator)
            f = new_numerator / new_denominator
            if f <= 1:
                percentage = int(f * 100)
                return percentage
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <=1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return(f"{percentage}%")


if __name__ == "__main__":
    main()
