def sum_natural_numbers(n):
    # If n is 0, return 0
    if n == 0:
        return 0
    # Recursion
    else:
        return n + sum_natural_numbers(n - 1)

# Input processing
n = int(input("Enter a natural number: "))

# Result output
result = sum_natural_numbers(n)
print(f"The sum of all natural numbers from 0 to {n} is: {result}")
