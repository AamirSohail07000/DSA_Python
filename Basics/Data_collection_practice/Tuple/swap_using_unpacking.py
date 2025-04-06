# Swap two numbers using tuple unpacking.

# Given two numbers
a = 5
b = 10

# Swapping using tuple unpacking
a, b = b, a  

# Printing the swapped values
print("After swapping:")
print("a =", a)
print("b =", b)

# NOTES:-
# How It Works?
# Before swapping:

# a = 5, b = 10

# Tuple packing:

# (b, a) creates a temporary tuple (10, 5).

# Tuple unpacking:

# a, b = 10, 5 assigns a = 10 and b = 5.