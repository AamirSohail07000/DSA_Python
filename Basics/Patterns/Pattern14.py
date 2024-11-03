# Print pattern 14
# A
# AB
# ABC
# ABCD
# ABCDE

n=5
def numToChr(num):
  return chr(num+65)
for i in range(n):
  for j in range(i+1):
    print(numToChr(j), end="")
  print()  

#   Explanation
# chr() Function:

# chr() is a built-in Python function that converts an ASCII code (integer) into its corresponding character.
# For example, chr(65) returns 'A' because 65 is the ASCII code for the letter 'A'.
# Offset Calculation (num + 65):

# Adding 65 to num shifts the input to match the ASCII codes for uppercase English letters:
# num = 0 → chr(0 + 65) = chr(65) = 'A'
# num = 1 → chr(1 + 65) = chr(66) = 'B'
# num = 2 → chr(2 + 65) = chr(67) = 'C'
