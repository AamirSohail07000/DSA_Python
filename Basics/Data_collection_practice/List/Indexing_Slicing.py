# Q-1  Given a list [10, 20, 30, 40, 50], print the second element from the end.


list1 = [10, 20, 30, 40, 50]
print(list1[(len(list1)-2)])

# Using Negative indexing

print(list1[-2])  # Output: 40

# Note: Python allows negative indexing, where -1 refers to the last element, -2 to the second-last

# Q2- Extract only even numbers from a given list [1, 2, 3, 4, 5, 6, 7, 8, 9]

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evenNumbers = []

for num in list2:
  if num % 2 == 0:  # Check if the number is even
    evenNumbers.append(num)  
print(evenNumbers) 