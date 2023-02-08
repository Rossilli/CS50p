import random


while True:
    try:
        level = input("Level: ")
        if level.isdigit():
            level = abs(int(level))
            random_level = random.randrange(1, level)
            break
        else:
            continue

    except ValueError:
        continue

while True:
    try:
        guess = input("Guess: ")
        if guess.isdigit():
            guess = abs(int(guess))
            if guess < random_level:
                print("Too small!")
                continue
            elif guess > random_level:
                print("Too large!")
                continue
            else:
                print("Just right!")
                break

    except ValueError:
        continue