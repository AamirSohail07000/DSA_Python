# Find the factorial of N (recursive + iterative)
# Concept n! = n × (n-1) × (n-2) … × 1


def factorial_recursive(n):
    """Find factorial of n using recursion"""
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """Find factorial of n using loop"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Example
print("Recursive:", factorial_recursive(5))
print("Iterative:", factorial_iterative(5))
