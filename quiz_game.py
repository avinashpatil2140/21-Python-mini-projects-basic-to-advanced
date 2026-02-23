print("Welcome to my Computer Quiz!")

playing = input("Do you want to play the quiz? (yes/no): ")

if playing.lower() != "yes":
    print("Maybe next time. Goodbye!")
    quit()

print("Okay! Let's play \n")

score = 0

# Question 1
answer = input("1. What is the capital of India? ")
if answer.lower() == "new delhi":
    print("Correct! ")
    score += 1
else:
    print("Wrong answer ")

# Question 2
answer = input("2. What is the capital of USA? ")
if answer.lower() in ["washington dc", "washington d.c.", "washington"]:
    print("Correct! ")
    score += 1
else:
    print("Wrong answer ")

# Question 3
answer = input("3. What is the capital of UK? ")
if answer.lower() == "london":
    print("Correct! ")
    score += 1
else:
    print("Wrong answer")

# Final Score
print("\nQuiz Completed!")
print("Your score is:", score, "/ 3")

percentage = (score / 3) * 100
print("You got", percentage, "% correct.")

              
    

