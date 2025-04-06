# Write a python program to Remove an element from a set and handle the case where the element might not exist. 

# Create a set with some elements
my_set = {10, 20, 30, 40, 50}

# Ask the user to enter the element to remove
element = int(input("Enter the element to remove: "))

# Use discard() to remove the element safely
my_set.discard(element)

# Show the updated set
print("Updated set:", my_set)
