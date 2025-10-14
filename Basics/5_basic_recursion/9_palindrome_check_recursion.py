# Check if the given String is Palindrome or not
# Recursive Approach

def is_palindrome_recursive(s: str, left: int, right: int) -> bool:
    """
    Function to check if a string is palindrome using recursion.
    """

    # Base case: crossed pointers or single char left
    if left >= right:
        return True

    # If characters mismatch → not a palindrome
    if s[left] != s[right]:
        return False

    # Recursive call for inner substring
    return is_palindrome_recursive(s, left + 1, right - 1)


# Example usage
string3 = "level"
string4 = "python"

print(f"{string3} → Palindrome? {is_palindrome_recursive(string3, 0, len(string3) - 1)}")
print(f"{string4} → Palindrome? {is_palindrome_recursive(string4, 0, len(string4) - 1)}")

