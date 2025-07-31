Number = int(input("Enter a Number: "))

# Initialize the factorial variable to 1
fact = 1

# Calculate the factorial using a for loop
for i in range(1, Number + 1):
    fact *= i

print(fact)

def factorial(n): 
    if (n==1 or n==0):
        
        return 1
    
    else:
        
        return (n * factorial(n - 1)) 
Number = int(input("Enter a Number: ")); 
print("number : ",Number)
print("Factorial : ",factorial(Number))