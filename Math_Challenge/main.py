import random
import time

OPERATORS = ['-','+','*']
MIN_OPERAND = 3
MAX_OPERAND = 10
TOTAL_QUESTIONS = 10

def generate_math():

    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " "  + str(right)
    answer = eval(expr)
    return expr, answer

user_star = input("Do you want to start the game (y/n)? ").lower()
if user_star == 'y':
    print()
    print("Lets start the challenge!!")
    print("---------------------------")
else:
    quit()

start_time = time.time()

wrong_ans = 0
for i in range(TOTAL_QUESTIONS):
    expr, answer = generate_math()
    while True:
        guess = input(f"Question {i+1}: {expr} = ")
        if guess == str(answer):
            break
        wrong_ans += 1

end_time = time.time()
total_time = round(end_time - start_time)
print("---------------------------")
print(f"Your number of wrong attempts: {wrong_ans}")
print(f"Nice work! You finished the challenge in {total_time} seconds")