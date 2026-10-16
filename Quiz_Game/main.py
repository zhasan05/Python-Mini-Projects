import requests as request
import json
import html
import random

def get_questions():
    url = "https://opentdb.com/api.php?amount=10&category=27&difficulty=easy&type=boolean"
    response = request.get(url)

    if response.status_code == 200:
        data = response.json()
        # pretty_json = json.dumps(data, indent=4)
        # print(pretty_json)
        result_list = data.get("results", [])

        all_questions = []
        for item in result_list:
            if "question" in item:
                raw_question = item.get("question")
                clean_question = html.unescape(raw_question)
                correct_answer = item.get("correct_answer") 
                all_questions.append({"question":clean_question, "answer": correct_answer})

        random.shuffle(all_questions)
        return all_questions
    
    else:
        None

print()
print("========== Welcome to Zee's Quiz Game ==========")
print()

user_input = input("Are you interested to play? ")
if user_input.lower() not in ["yes", "y"]:
    quit()
else:
    score = 0
    questions = get_questions()

    if questions:
        for i, q in enumerate(questions):
            print(f"\nQuestion {i+1}: {q['question']}")
            user_input = input("True or False? ").strip()

            if user_input.lower() == q["answer"].lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {q['answer']}.")
        print(f"\n Game Over! Final Score: {score}/{len(questions)}")
    else:
        print("Could not retrieve questions. Please check your connection.")