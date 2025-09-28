def factorial_recursive(x):
    """
    Recursive approach to calculate factorial.
    """

    # Base case: factorial of 0 or 1 is 1
    if x == 0 or x == 1:
        return 1

    # Recursive case: x! = x * (x-1)!
    return x * factorial_recursive(x - 1)


# Example usage
X = int(input("Enter a number: ")) # Or use value like X = 5 
print(f"Factorial of {X} using recursion:", factorial_recursive(X))
