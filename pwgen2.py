import random
import string

def generate_password(min_length , numbers = True , symbols = True):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    characters = letters
    
    if numbers:
        characters += digits
    if symbols:
        characters += symbols
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_symbol = False
    
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
    
        if new_char in digits:
            has_number = True
        if new_char in symbols:
            has_symbol = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if symbols:
            meets_criteria =meets_criteria and has_symbol 
        
    return pwd
    
min_length = int(input("Enter the minimum length : "))
has_number = input("Do you want to have numbers ? (y/n) ").lower() == "y"
has_symbol = input("Do you want to have symbols ? (y/n) ").lower() == "y"
pwd = generate_password(min_length, has_number , has_symbol)
print("This is your password ", pwd)