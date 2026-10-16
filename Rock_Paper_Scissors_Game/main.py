import random

options = ["rock", "paper", "scissors"]

user_score = 0
system_score = 0

while True:
    prompt = print("Please choose 'Rock/Paper/Scissors' to play or 'Q' to quit")

    user_input = input("Enter your choice here: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid input!")
        continue

    rand_option = random.randint(0,2)
    system_choice = options[rand_option]

    if user_input == 'rock' and system_choice == 'scissors':
        print(f"You won! Computer picked - {system_choice}\n")
        user_score += 1 

    elif user_input == 'paper' and system_choice == 'rock':
            print(f"You won! Computer picked - {system_choice}\n")
            user_score += 1 

    elif user_input == 'scissors' and system_choice == 'paper':
            print(f"You won! Computer picked - {system_choice}\n")
            user_score += 1 
    else:
         print(f"You lost! Computer picked - {system_choice}\n")
         system_score += 1

print()
print("Thank you for playing!")
print()
print(f"Your total score is {user_score}")
print(f"Computer's total score is {system_score}")
print()
print("See you next time!")