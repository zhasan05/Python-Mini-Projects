import string
import random

def generate_password(min_length, digits=False, special_characters=False):
    characters = string.ascii_letters # values A-Z and a-z
    nums = string.digits # values (0-9)
    spec_chars = string.punctuation # values (!@#$%^&*)

    if digits:
        characters += nums
    if special_characters:
        characters += spec_chars

    password = ""
    pass_criteria = False
    has_digits = False
    has_spec_chars = False

    while not pass_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in nums:
            has_digits = True
        elif new_char in spec_chars:
            has_spec_chars = True

        pass_criteria = True
        if digits:
            pass_criteria = has_digits
        if special_characters:
            pass_criteria = pass_criteria and has_spec_chars
    return password

user_pass_len = int(input("Enter your password length: "))
user_pass_num = input("Type (y/n) if you want numbers in your password: ").lower()
user_pass_special = input("Type (y/n) if you want special characters in your password: ").lower()

if user_pass_num == 'y':
    user_has_num = True
else:
    user_has_num = False

if user_pass_special == 'y':
    user_has_spec_char = True
else:
    user_has_spec_char = False

pswd = generate_password(user_pass_len, user_has_num, user_has_spec_char)
print(f"This is your new password: {pswd}")