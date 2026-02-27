name = input("What is your name? ")
print(name + ", welcome to the Adventure Game!")

answer = input(
    "You are in a forest and want to go out but you see two roads: left and right. "
    "Which way do you wanna go? (left/right) "
)

if answer.lower() == "left":
    answer = input(
        "You reached a river. Do you want to swim or wait for a boat? (swim/wait) "
    )

    if answer.lower() == "wait":
        print("You waited for a boat and reached the other side of the river safely.")

        answer = input(
            "You see a house. Do you want to go inside or keep walking? (inside/walk) "
        )

        if answer.lower() == "inside":
            print("You entered the house and found a treasure chest.")
            print("You opened the chest and found a lot of gold coins.")
            print("Congratulations! You win the game.")
        else:
            print("You kept walking and got lost in the forest.")
            print("Game over!")

    else:
        print("You tried to swim but got caught in the current and drowned.")
        print("Game over!")

else:
    print("You took the right path and got lost in the forest.")
    print("Game over!")
