def factorial(n):
    # Base case: Factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: Multiply n with factorial of (n-1)
    else:
        return n * factorial(n - 1)
print(factorial(6))
