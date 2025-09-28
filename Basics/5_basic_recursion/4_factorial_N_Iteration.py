# Problem Statement: Given a number X,  print its factorial.
# To obtain the factorial of a number, it has to be multiplied by all the whole numbers preceding it. More precisely X! = X*(X-1)*(X-2) … 1.
# Note: X  is always a positive number. 

def factorial_iterative(x):
    """
    Iterative approach to calculate factorial.
    """
    result = 1

    # Multiply numbers from 1 to x
    for i in range(1, x + 1):
        result *= i

    return result


# Example usage
X = 5
print(f"Factorial of {X} using iteration:", factorial_iterative(X))
