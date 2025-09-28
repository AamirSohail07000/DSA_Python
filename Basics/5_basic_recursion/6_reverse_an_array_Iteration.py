# Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

# Iterative (Two-Pointer Approach)
def reverse_array_iterative(arr):
    """
    Function to reverse an array in-place using iteration (two-pointer method).
    """
    left, right = 0, len(arr) - 1

    while left < right:
        # Swap elements at left and right indices
        arr[left], arr[right] = arr[right], arr[left]

        # Move pointers towards the center
        left += 1
        right -= 1

    return arr


# Example usage
arr = [1, 2, 3, 4, 5]
print("Original array:", arr)
reverse_array_iterative(arr)
print("Reversed array :", arr)

