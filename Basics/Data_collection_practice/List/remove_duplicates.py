# Write a Python program to remove duplicate elements from a list.

# Method 1 using set()

numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_numbers = list(set(numbers))
print(unique_numbers)

# Method 2: Using a loop (Preserves Order)
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)

