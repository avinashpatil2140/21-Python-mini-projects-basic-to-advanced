import random

r = random.randint(0, 10)

while True:
    try:
        choosed_number = int(input("Choose a number between 0 and 10: "))

        if choosed_number < 0 or choosed_number > 10:
            print("Please choose a number between 0 and 10.")
            continue

        if choosed_number == r:
            print("Congratulations! You guessed it right ")
            break
        elif choosed_number < r:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    except ValueError:
        print("Please enter a valid number!")


