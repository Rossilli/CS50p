def main():
    greet = input("Greeting: ")
    greeting = value(greet)
    print(f"${greeting}")

def value(greeting):
    greeting = greeting.lower().replace(" ", "")
    if "hello" in greeting:
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()