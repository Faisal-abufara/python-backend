def FindEvenNumber(Number):
    if(Number %2==0):
        return "Even"
    else:
        return "Odd"

def AddThemNumbers(Number1, Number2):
    if not isinstance(Number1, (int, float)) or not isinstance(Number2, (int, float)):
        raise TypeError("Both inputs must be numbers (int or float)")
    return Number1 + Number2

print(AddThemNumbers(4,5))
print(FindEvenNumber(10))