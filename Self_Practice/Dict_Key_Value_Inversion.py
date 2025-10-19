# Question: Given a dictionary where values might be duplicated, return a new dictionary where the values of the original dictionary become the keys of the new dictionary, and the corresponding new value is a list of the original keys that mapped to that value.

def invert_dictionary(input_dict):
    """Inverts a dictionary, grouping original keys by their value."""
    inverted_dict = {}
    for key, value in input_dict.items():
        # Use a list to store multiple keys that map to the same value
        if value not in inverted_dict:
            inverted_dict[value] = []
        inverted_dict[value].append(key)
    return inverted_dict

# Example Usage:
data_dict = {'Math': 95, 'Science': 90, 'History': 95, 'Art': 88, 'English': 90}
print("\n--- Dictionary & List: Key-Value Inversion ---")
print(f"Original Dict: {data_dict}")
print(f"Inverted Dict: {invert_dictionary(data_dict)}")
# Expected: {95: ['Math', 'History'], 90: ['Science', 'English'], 88: ['Art']}