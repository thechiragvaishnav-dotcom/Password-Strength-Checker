import string  # For checking character diversity
import getpass  # For secure password input
import math  # For entropy calculation

# Minimum recommended password length
MIN_LENGTH = 8  

def calculate_entropy(password):
    """Calculates entropy based on character diversity and length."""
    charset_size = 0
    if any(c in string.ascii_lowercase for c in password):
        charset_size += 26
    if any(c in string.ascii_uppercase for c in password):
        charset_size += 26
    if any(c in string.digits for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)
    if any(c.isspace() for c in password):
        charset_size += 1
    
    return len(password) * math.log2(charset_size) if charset_size else 0

def check_password_strength():
    """Evaluates password strength based on entropy and diversity."""
    password = getpass.getpass('Enter your password: ')
    
    if len(password) < MIN_LENGTH:
        print(f" Your password is too short! It must be at least {MIN_LENGTH} characters.")
        return

    lower_count = sum(1 for c in password if c in string.ascii_lowercase)
    upper_count = sum(1 for c in password if c in string.ascii_uppercase)
    num_count = sum(1 for c in password if c in string.digits)
    special_count = sum(1 for c in password if c in string.punctuation)
    wspace_count = sum(1 for c in password if c.isspace())
    
    entropy = calculate_entropy(password)
    
    # Classifying password strength
    if entropy < 28:
        remarks = " Very Weak: Easily guessable! Change it immediately."
    elif entropy < 36:
        remarks = " Weak: Can be cracked quickly. Use a stronger password."
    elif entropy < 60:
        remarks = " Moderate: Decent password, but can still be improved."
    elif entropy < 80:
        remarks = " Strong: Hard to guess, but consider making it longer."
    else:
        remarks = " Very Strong: Excellent password! Highly secure."
    
    # Display password analysis
    print("\n Password Analysis:")
    print(f" {lower_count} lowercase letters")
    print(f" {upper_count} uppercase letters")
    print(f" {num_count} digits")
    print(f" {special_count} special characters")
    print(f" {wspace_count} whitespace characters")
    print(f" Entropy Score: {entropy:.2f} bits")
    print(f" Remarks: {remarks}\n")

def check_another_password():
    """Asks the user if they want to check another password."""
    while True:
        choice = input(" Do you want to check another password? (y/n): ").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            print(" Exiting... Stay secure!")
            return False
        else:
            print(" Invalid input. Please enter 'y' or 'n'.")

if __name__ == '__main__':
    print("=====  Welcome to Password Strength Checker  =====")
    check_password_strength()
    while check_another_password():
        check_password_strength()