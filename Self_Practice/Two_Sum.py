# Question: Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target. Assume that each input has exactly one solution, and you may not use the same element twice.

def two_sum(nums, target):
    """
    Finds the indices of two numbers in an array that sum up to a target.
    Uses a dictionary (hash map) for O(n) time complexity.
    """
    num_map = {}  # {number: index}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index
    return []

# Example Usage:
print("--- Two Sum ---")
print(f"Indices: {two_sum([2, 7, 11, 15], 9)}") 
print(f"Indices: {two_sum([3, 2, 4], 6)}")      