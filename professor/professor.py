import random

def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        for j in range(3):
            answer = input(f"{x} + {y} = ")
            if is_number(answer) and int(answer) == correct_answer:
                score += 1
                break
            else:
                print("EEE")
        else:
            print(f"{correct_answer}")
    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Enter a level (1, 2, or 3): ")
        if level in ["1", "2", "3"]:
            return int(level)
        else:
            print("Invalid input. Please try again.")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level.")

def is_number(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
