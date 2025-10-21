# Write a function that takes two variables, a and b, and uses a tuple to swap their values in a single line

def swap_variables(a, b):
    """Swaps the values of two variables using tuple packing/unpacking."""
    print(f"Before Swap: a={a}, b={b}")
    
    # The core tuple swapping technique
    a, b = b, a
    
    print(f"After Swap: a={a}, b={b}")
    return a, b

# Example Usage:
print("\n--- Tuple: Immutability and Swapping ---")
val_a = 100
val_b = "Hello"
swap_variables(val_a, val_b)