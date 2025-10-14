# Check if the given String is Palindrome or not
# Iterative (Two-Pointer Approach

def is_palindrome_iterative(s: str) -> bool:
    """
    Function to check if a string is palindrome using iteration.
    Uses two-pointer technique: one pointer at the start, one at the end.
    """

    left, right = 0, len(s) - 1

    while left < right:
        # Compare characters at both ends
        if s[left] != s[right]:
            return False  # If mismatch, not a palindrome

        # Move pointers closer
        left += 1
        right -= 1

    return True  # No mismatches found


# Example usage
string1 = "madam"
string2 = "hello"

print(f"{string1} → Palindrome? {is_palindrome_iterative(string1)}")
print(f"{string2} → Palindrome? {is_palindrome_iterative(string2)}")
