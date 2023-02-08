import random

rps = ["rock", "paper", "scissor"]


def main():
    user1 = pick()
    cpu1 = random_cpu()
    winner = play(user1, cpu1)
    print(winner)


def pick():
    user = input("Choose Rock, Paper or Scissor: ").lower()
    while user not in rps:
        user = input("Incorrect input try again: ").lower()
    return user


def random_cpu():
    cpu_choice = random.choice(rps)
    print(f"Your opponent chooses {cpu_choice}")
    return cpu_choice


def play(user1, cpu1):
    if user1 == cpu1:
        return "Tie!"
    elif user1 == "paper" and cpu1 == "rock":
        return "You win"
    elif user1 == "rock" and cpu1 == "scissor":
        return "You win"
    elif user1 == "scissor" and cpu1 == "paper":
        return "You win"
    else:
        return "You lose"


if __name__ == "__main__":
    main()