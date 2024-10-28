def fibonacci(n):
    # Fibonacci of 0 is 0, Fibonacci of 1 is 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursion
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input processing
n = int(input("Enter a non-negative integer to calculate its Fibonacci value: "))

# Result output
result = fibonacci(n)
print(f"The Fibonacci value of {n} is: {result}")
