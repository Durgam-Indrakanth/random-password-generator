import random
import string

def ask_choice(message):
    while True:
        choice = input(message).lower()
        if choice in ["y", "n"]:
            return choice == "y"
        else:
            print("Invalid input! Please enter only 'y' or 'n'.")

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected."

    password = "".join(random.choice(characters) for _ in range(length))
    return password

print("\n--- Passwword Generator ---\n")

try:
    length = int(input("Enter password length: "))
except ValueError:
    print("Invalid input! please enter a number.")
    exit()

print("\nChoose character types to include in the password:")
use_upper = ask_choice("Include uppercase letters? (y/n): ")
use_lower = ask_choice("Include lowercase letters? (y/n): ")
use_digits = ask_choice("Include digits? (y/n): ")
use_symbols = ask_choice("Include symbols? (y/n): ")

password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

print("\nGenerated Password:", password)
print("\nDone!")