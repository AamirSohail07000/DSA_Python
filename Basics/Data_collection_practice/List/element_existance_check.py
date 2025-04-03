# Check if an element exists in the list without using in keyword.

# Method 1: Using a Loop
def element_exists(lst, target):
    for item in lst:
        if item == target:
            return True
    return False

# Example Usage
numbers = [1, 2, 3, 4, 5]
target = 3

if element_exists(numbers, target):
    print(f"{target} exists in the list.")
else:
    print(f"{target} does not exist in the list.")

# Method 2: Using count() Function

def element_exists(lst, target):
    return lst.count(target) > 0

# Example Usage
numbers = [1, 2, 3, 4, 5]
target = 6

if element_exists(numbers, target):
    print(f"{target} exists in the list.")
else:
    print(f"{target} does not exist in the list.")
