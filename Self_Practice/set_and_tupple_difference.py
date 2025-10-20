# Given two lists, list_a and list_b, determine if they share no common elements (i.e., their intersection is empty). Return True if they are completely distinct, and False otherwise. (Hint: Convert them to sets for efficient comparison).

def are_lists_distinct(list_a, list_b):
    """Checks if two lists have any common elements using set difference."""
    set_a = set(list_a)
    set_b = set(list_b)
    
    # Check if the intersection of the two sets is empty
    return set_a.isdisjoint(set_b)

# Example Usage:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [3, 7, 8]

print("\n--- Set & Tuple: Difference Check ---")
print(f"List 1 ({list1}) and List 2 ({list2}) are distinct: {are_lists_distinct(list1, list2)}")
# Expected: True
print(f"List 1 ({list1}) and List 3 ({list3}) are distinct: {are_lists_distinct(list1, list3)}")
# Expected: False