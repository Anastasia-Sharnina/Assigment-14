def sum_of_digits(n):
    # If n is 0, return 0
    if n == 0:
        return 0
    # Recursion
    else:
        return (n % 10) + sum_of_digits(n // 10)

# Input processing
n = int(input("Enter a natural number: "))

# Result output
result = sum_of_digits(n)
print(f"The sum of the digits of {n} is: {result}")
