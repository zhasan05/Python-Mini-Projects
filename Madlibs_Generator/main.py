# open the text and save it to story
with open("story.txt", 'r') as file:
    story = file.read()
# print(story)

words = set()
start_index = -1

# save the list of words in a set
for i, char in enumerate(story):
    if char == "<":
        start_index = i
    if char == ">" and start_index != -1:
        word = story[start_index: i+1]
        words.add(word)
        start_index = -1
# print(words)

# save user answer in an answer dictionary
answers = {}
for word in words:
    user_answer = input(f"Enter a word for {word}: ")
    answers[word] = user_answer
# print(answers)

# replace the words in the story and save it
for word in answers:
    story = story.replace(word, answers[word])

print("\nCompleted Story:\n")
print(story)
