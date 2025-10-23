# Find maximum element in an array (recursion)

def find_max(arr, n):
    """Find maximum element in array using recursion"""
    if n == 1:
        return arr[0]
    return max(arr[n - 1], find_max(arr, n - 1))

# Example
arr = [3, 7, 2, 9, 5]
print("Maximum element:", find_max(arr, len(arr)))
