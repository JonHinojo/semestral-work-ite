'''interface for the password strength checker'''

from src.password_checker import evaluate_password


def main():
    '''asks for a password and then show what its strenght is'''
    
    while True:
        password = input ("Enter a passwrod: ")
        try:
            level, reasons = evaluate_password(password)
            break
        
        except ValueError as error: # only when spaces or blank
            print(error)
        
    if reasons:
            print(level + ": " + " and ".join(reasons))
    else:
            print(level)
            
if __name__ == "__main__":
    main()