# Given a list of integers, create a new list containing only the squares of the even numbers.

def square_even_numbers(numbers):
    """Filters for even numbers and returns a list of their squares."""
    # Using list comprehension for a concise solution
    squared_evens = [x**2 for x in numbers if x % 2 == 0]
    return squared_evens

# Example Usage:
data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("--- List: Filtering and Transformation ---")
print(f"Original List: {data_list}")
print(f"Squared Evens: {square_even_numbers(data_list)}")
# Expected: [4, 16, 36, 64, 100]