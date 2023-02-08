def main():
    plate = input("plate: ")
    plate = plate.upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if 2 <= len(plate) <= 6 and plate[0:2].isalpha() and plate.isalnum():
        for i in plate:
            if i.isdigit():
                index = plate.index(i)
                if plate[index:].isdigit() and int(i) != 0:
                    return True
                else:
                    return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()