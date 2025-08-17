def positive_numbers_only(func):
    def wrapper(*args, **kwargs):
    
        for i, arg in enumerate(args):
            if not (isinstance(arg, (int, float)) and arg > 0):
                raise ValueError(f"Argument #{i+1} ({arg}) is not a positive number")

        
        for key, value in kwargs.items():
            if not (isinstance(value, (int, float)) and value > 0):
                raise ValueError(f"Argument '{key}' ({value}) is not a positive number")

        return func(*args, **kwargs)
    return wrapper


@positive_numbers_only
def AddTwoNumbers(a,b):
    return a+b

print(AddTwoNumbers(5,10))
print(AddTwoNumbers(10,20))