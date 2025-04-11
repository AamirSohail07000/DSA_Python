# Create a dictionary where keys are numbers from 1 to 5 and values are their squares.

# Create a dictionary using dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}

# Print the dictionary
print(squares)


# Note: Dictionary comprehension is a concise and elegant way to create dictionaries in a single line of code using a for loop.
# Syntax:   {key_expression: value_expression for item in iterable}


# Lambda vs Dictionary comprehension
# Feature	Dictionary Comprehension	Lambda Function
# 📌 Use Case	To create dictionaries from iterables	To create small, anonymous functions
# 🔤 Syntax	{key: value for item in iterable}	lambda arguments: expression
# 💡 Example	{x: x**2 for x in range(1, 4)} → {1: 1, 2: 4, 3: 9}	lambda x: x**2 → returns square of x
