# Divide array into halves — check middle element. (Recursive)

def binary_search(arr, left, right, target):
    """Recursive binary search"""
    if left > right:
        return -1  # Element not found

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)


# Example
arr = [2, 4, 6, 8, 10, 12]
target = 10
print("Element found at index:", binary_search(arr, 0, len(arr) - 1, target))
