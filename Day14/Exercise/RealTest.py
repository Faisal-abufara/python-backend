def AddThemNumbers(Number1, Number2):
    if not isinstance(Number1, (int, float)) or not isinstance(Number2, (int, float)):
        raise TypeError("Both inputs must be numbers (int or float)")
    return Number1 + Number2

def SubtractNumbers(Number1, Number2):
    return Number1 - Number2

def IsEven(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be a number")
    return num % 2 == 0
