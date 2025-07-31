def generate_fibonacci(n):
    fib_series = []
    a, b = 0, 1

    for i in range(n):
        fib_series.append(a)
        a, b = b, a + b

    return fib_series


num_terms = int(input("Enter the number of terms in Fibonacci series: "))

# Generate and display the Fibonacci series
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    series = generate_fibonacci(num_terms)
    print("Fibonacci series:")
    print(series)
