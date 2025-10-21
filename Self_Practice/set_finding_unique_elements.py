# Question: Given a list that may contain duplicate elements, return a list of only the unique elements, preserving the original order of first appearance as much as possible.

def get_unique_in_order(data):
    """Returns a list of unique elements from the input list using a set."""
    seen = set()
    result = []
    
    for item in data:
        if item not in seen:
            result.append(item)
            seen.add(item)
            
    return result

# Example Usage:
data_with_duplicates = [1, 5, 2, 1, 3, 5, 4, 2, 6]
print("\n--- Set: Finding Unique Elements ---")
print(f"Original Data: {data_with_duplicates}")
print(f"Unique Elements (Order Preserved): {get_unique_in_order(data_with_duplicates)}")
# Expected: [1, 5, 2, 3, 4, 6]