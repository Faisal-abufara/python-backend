def _validate_input(Number1, Number2):
    if not isinstance(Number1, (int, float)) or not isinstance(Number2, (int, float)):
        raise TypeError("Both inputs must be numbers (int or float)")

def AddThemNumbers(Number1, Number2):
    _validate_input(Number1, Number2)
    return Number1 + Number2
