# Find the key with the highest value in a dictionary { "A": 50, "B": 75, "C": 20 }.


scores = { "A": 50, "B": 75, "C": 20 }

# Use max() with key=scores.get to find the key with the highest value
max_key = max(scores, key=scores.get)

print("Key with the highest value:", max_key)


# Explaination
# max(scores, key=scores.get) means:
# Check each key in the dictionary.
# Use its corresponding value (from scores.get) to compare.
# Return the key with the highest value.