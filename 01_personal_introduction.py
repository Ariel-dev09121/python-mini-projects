# Program 1: Personal Introduction (final version)

# --- Reusable "recipes" (functions) ---

def ask_text(question):
    """Keeps asking until the answer has only letters."""
    while True:
        answer = input(question)
        if answer.replace(" ", "").isalpha():
            return answer.strip().title()
        print("Please use only letters.")

def ask_age(question):
    """Keeps asking until the age is a number from 1 to 120."""
    while True:
        answer = input(question)
        if answer.isdigit() and 1 <= int(answer) <= 120:
            return int(answer)
        print("Please enter a valid age (1-120).")

# --- Main program ---

name = ask_text("What is your name? ")
age = ask_age("How old are you? ")
country = ask_text("What country do you live in? ")
food = ask_text("What is your favorite food? ")
color = ask_text("What is your favorite color? ")
hobby = ask_text("What is your hobby? ")

print()
print("===== About Me =====")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Country: {country}")
print(f"Favorite food: {food}")
print(f"Favorite color: {color}")
print(f"Next year I will be {age + 1} years old.")
print(f"My hobby is {hobby}")
