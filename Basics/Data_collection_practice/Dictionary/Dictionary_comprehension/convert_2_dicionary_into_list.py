# Convert two lists into a dictionary using comprehension:

keys = ['a', 'b', 'c']
values = [1, 2, 3]

# Given lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]

# Creating dictionary using comprehension and zip
result = {k: v for k, v in zip(keys, values)}

# Printing the result
print(result)
