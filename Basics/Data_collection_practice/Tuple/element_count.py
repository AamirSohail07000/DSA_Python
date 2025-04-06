# Write a python program to Count how many times an element appears in a tuple.

# Define the tuple
my_tuple = (1, 2, 3, 2, 4, 2, 5, 1)

# Ask the user for the element to count
element = int(input("Enter the element to count: "))

# Use the count() method
count = my_tuple.count(element)

# Display the result
print(f"The element {element} appears {count} times in the tuple.")
