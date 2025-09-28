def reverse_array_recursive(arr, left, right):
    """
    Function to reverse an array in-place using recursion.
    """

    # Base case: stop when pointers cross each other
    if left >= right:
        return

    # Swap elements at left and right
    arr[left], arr[right] = arr[right], arr[left]

    # Recursive call for the next inner subarray
    reverse_array_recursive(arr, left + 1, right - 1)


# Example usage
arr2 = [10, 20, 30, 40, 50]
print("Original array:", arr2)
reverse_array_recursive(arr2, 0, len(arr2) - 1)
print("Reversed array :", arr2)
