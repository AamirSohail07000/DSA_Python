# Given a list of strings, count the frequency of each unique string and return the result as a dictionary, where keys are the strings and values are their counts.

def count_word_frequency(words):
    """Counts the frequency of each word in a list."""
    frequency = {}
    for word in words:
        # Get the current count (defaulting to 0 if key doesn't exist) and increment
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Example Usage:
word_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
print("\n--- Dictionary: Aggregation (Counting Frequency) ---")
print(f"Word List: {word_list}")
print(f"Frequencies: {count_word_frequency(word_list)}")
# Expected: {'apple': 3, 'banana': 2, 'orange': 1}