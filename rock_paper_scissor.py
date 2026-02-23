import random

while True:
    try:
        
        c = random.choice(["rock", "paper", "scissor"])

        user_input = input("choose rock, paper or scissor: ").lower()

        if user_input not in ["rock", "paper", "scissor"]:
            raise ValueError

        print("Computer chose:", c)

        if user_input == c:
            print("its tie")
        elif user_input == "rock" and c == "scissor":
            print("you win")
        elif user_input == "paper" and c == "rock":
            print("you win")
        elif user_input == "scissor" and c == "paper":
            print("you win")
        else:
            print("you lose")

    except ValueError:
        print("Please enter a valid input!")
