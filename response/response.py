from validator_collection import validators

def main():
    print(validator(input("Email: ")))


def validator(email):
    try:
        email =  validators.email(email)
        return "Valid"
    except ValueError:
        return "Invalid"


if __name__ == "__main__":
    main()