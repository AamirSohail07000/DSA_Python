# Merge two dictionaries { "a": 1, "b": 2 } and { "c": 3, "d": 4 }.

# Method 1: Using the update() method

dict1 = { "a": 1, "b": 2 }
dict2 = { "c": 3, "d": 4 }

# Copy dict1 to avoid modifying the original
merged_dict = dict1.copy()

# Update with dict2
merged_dict.update(dict2)

print("Merged Dictionary:", merged_dict)
