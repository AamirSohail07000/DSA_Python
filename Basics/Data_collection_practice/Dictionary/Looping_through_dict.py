# Print all keys and values of a dictionary using a loop.

# Dictionary with student names and their scores
student_scores = {
    "Alice": 85,
    "Bob": 95,
    "Charlie": 78
}

# Loop through the dictionary and print keys and values
for name, score in student_scores.items():
    print("Name:", name, ", Score:", score)

# Note: .items() returns a view of key-value pairs (tuples) from the dictionary.
# for name, score in student_scores.items() unpacks each key-value pair and prints them.