# Finding Unique Elements
# Given a list with duplicates [1, 2, 2, 3, 4, 4, 5], remove duplicates using a set.

my_list = [1, 2, 2, 3, 4, 4, 5]

# Convert the list to a set to remove duplicates
unique_set = set(my_list)

# Optional: Convert back to a list if needed
unique_list = list(unique_set)

print("List after removing duplicates:", unique_list)
