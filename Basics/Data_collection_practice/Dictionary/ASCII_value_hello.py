# Create a dictionary of characters and their ASCII values using a string "hello".

text = "hello"

ascii_dict = {char: ord(char) for char in text}

print(ascii_dict)
