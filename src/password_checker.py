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
    