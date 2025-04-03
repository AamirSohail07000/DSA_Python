# Given a tuple (1, 2, 3, 4, 5), print the third element.

# Given tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing the third element (index 2)
third_element = my_tuple[2]

# Printing the third element
print("Third element:", third_element)


# Extract the first three elements of a given tuple.

# Given tuple
my_tuple = (10, 20, 30, 40, 50)

# Extracting the first three elements using slicing
first_three = my_tuple[:3]

# Printing the extracted elements
print("First three elements:", first_three)

# Note: Slicing is a technique used to extract a portion of a sequence (like a list, tuple, or string) using the start:stop:step format.
# Syntax - sequence[start:stop:step]
# my_tuple[:3] means:
# Start from index 0 (default).

# Stop at index 3 (not included).

# Default step is 1 (move one by one).

# So, it extracts elements at index 0, 1, and 2 → (10, 20, 30).
