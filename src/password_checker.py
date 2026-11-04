import string
import os

"""Functions to evaluate the strength of a password"""

def check_length(password):
    """Give points based on the length of the password.
    Returns the points (0 to 2) and a list of reasons
    explaining what is missing.
    """
    length = len(password)

    if length >= 12:
        return 2, []
    elif length >= 8:
        return 1, ["shorter than 12 characters"]
    else:
        return 0, ["shorter than 8 characters"]
    
    
def check_character_types(password):
    '''give one point for each type of character in the password
    
    returns the points (0 to 4) and a list of reasons explaining what is missing'''
    
    points = 0
    reasons =[]
    
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False
    
    for char in password:
        if char.islowe():
            has_lower = True
        if char.isipper():
            has_upper = True
        if char.isdigit():
            has_digit = True
        if char in string.punctuation:
            has_symbol = True
    if has_lower:
        points += 1
    else:
        reasons.append("no lowercase letters")
        
    if has_upper:
        points += 1
    else:
        reasons.append("no uppercase letters")
        
    if has_upper:
        points += 1
    else:
        reasons.append("no digits")
        
    if has_upper:
        points += 1
    else:
        reasons.append("no symbols")
        
    return points, reasons



def is_common_password(password):
    '''return true if the password is in the common list'''
    file_path = os.path.join(os.path.dirname(__file__), "..","data", "common_passwords.txt")
    
    with open(file_path, "r", encoding="utf-8") as file:
        common_passwords = file.read().lower().splitlines()
        
    return password.lower() in common_passwords
    
