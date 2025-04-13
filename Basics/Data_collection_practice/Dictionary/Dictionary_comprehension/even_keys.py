# From a dictionary {1: 2, 2: 5, 3: 6, 4: 8}, create a new dictionary with only the keys that have even values.

# Original dictionary
original_dict = {1: 2, 2: 5, 3: 6, 4: 8}

# Creating a new dictionary with only even values
even_values_dict = {k: v for k, v in original_dict.items() if v % 2 == 0}

# Printing the result
print(even_values_dict)
