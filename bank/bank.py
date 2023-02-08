def main():
    greet = input("Greeting: ")
    greet = greet.lower().replace(" ", "")
    greet = value(greet)
    print(f"{greet}")

def value(greeting):
    if "hello" in greeting:
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()