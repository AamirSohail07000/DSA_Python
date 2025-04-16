# Reverse a dictionary using dictionary comprehension:  python CopyEdit original = {'a': 1, 'b': 2, 'c': 3} # Output: {1: 'a', 2: 'b', 3: 'c'} 

original = {'a': 1, 'b': 2, 'c': 3}

# Reverse the dictionary: keys become values and values become keys
reversed_dict = {value: key for key, value in original.items()}

print(reversed_dict)
