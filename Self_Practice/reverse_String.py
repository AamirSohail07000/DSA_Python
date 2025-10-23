# Reverse a string using recursion
# Concept:
# Swap first and last character, recurse for middle substring.

def reverse_string(s):
    """Reverse string recursively"""
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])


# Example
s = "hello"
print("Reversed string:", reverse_string(s))
