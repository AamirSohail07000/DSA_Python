# Create a dictionary of characters and their ASCII values using a string "hello".

text = "hello"

ascii_dict = {char: ord(char) for char in text}

print(ascii_dict)


# ✅ ord(char)
# The ord() function in Python returns the ASCII (or Unicode) code of the given character.

# For example:

# ord('h') → 104

# ord('e') → 101

# ord('l') → 108

# ord('o') → 111

# ✅ {char: ord(char) for char in text}
# This creates key-value pairs where:

# key → character (like 'h')

# value → its ASCII code (like 104)