# Given a list of numbers, find the second largest number.

# Method 1: Using sort() (Simple but modifies the list)

numbers = [10, 20, 4, 45, 99, 99]
numbers = list(set(numbers))  # Remove duplicates
numbers.sort()  # Sort the list in ascending order
print("Second largest number:", numbers[-2])  # Second last element

# Method 2: Using Loop (Efficient, Does not modify list)
numbers = [10, 20, 4, 45, 99, 99]

first = second = float('-inf')  # Initialize first and second largest as negative infinity

for num in numbers:
    if num > first:
        second = first  # Update second largest
        first = num  # Update first largest
    elif num > second and num != first:
        second = num  # Update second largest if num is not equal to first largest

print("Second largest number:", second)

# Method 3: Using heapq.nlargest() (One-liner)

import heapq
numbers = [10, 20, 4, 45, 99, 99]
second_largest = heapq.nlargest(2, set(numbers))[1]  # Get top 2 unique numbers
print("Second largest number:", second_largest)


# Note:- The heapq module in Python provides an implementation of the heap queue algorithm, also known as the priority queue. It is useful for efficiently retrieving the smallest or largest elements from a collection.

# heapq uses a binary heap, which is a complete binary tree that satisfies the heap property:

# Min-Heap (default in Python): The parent node is always ≤ its child nodes.

# Max-Heap (not default, but can be implemented): The parent node is always ≥ its child nodes.

# OPERATIONS

# Convert a List into a Heap
# Use heapq.heapify() to transform a list into a min-heap.
# import heapq

# numbers = [5, 1, 8, 3, 2]
# heapq.heapify(numbers)  
# print(numbers)  # Output: [1, 2, 8, 3, 5] (Heap order)


# Insert an Element into the Heap
# Use heapq.heappush() to add an element while maintaining the heap structure.
# heapq.heappush(numbers, 0)
# print(numbers)  # Output: [0, 1, 8, 3, 5, 2]


# Remove and Return the Smallest Element
# Use heapq.heappop() to remove the smallest element.
# smallest = heapq.heappop(numbers)
# print(smallest)  # Output: 0
# print(numbers)   # Remaining heap: [1, 2, 8, 3, 5]


# Pop and Insert a New Element
# Use heapq.heapreplace(), which removes the smallest element and inserts a new one in one step.
# heapq.heapreplace(numbers, 7)
# print(numbers)  # Output: [2, 3, 8, 7, 5]


# Instead of sorting the entire list, use:

# heapq.nlargest(n, iterable): Get the n largest elements.

# heapq.nsmallest(n, iterable): Get the n smallest elements.
# numbers = [10, 20, 4, 45, 99, 8]

# largest_two = heapq.nlargest(2, numbers)
# print(largest_two)  # Output: [99, 45]

# smallest_two = heapq.nsmallest(2, numbers)
# print(smallest_two)  # Output: [4, 8]


# Since Python’s heapq only supports min-heaps, we can simulate a max-heap by storing negative values.
# max_heap = []
# heapq.heappush(max_heap, -10)
# heapq.heappush(max_heap, -20)
# heapq.heappush(max_heap, -5)

# largest = -heapq.heappop(max_heap)
# print(largest)  # Output: 10 (largest element)
