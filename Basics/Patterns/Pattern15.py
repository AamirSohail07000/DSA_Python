# print pattern-15
# ABCDE
# ABCD
# ABC
# AB
# A
n= 5
def numToChr(num):
  return chr(num + 65)
for i in range(n):
  for j in range (n-i):
    print(numToChr(j), end="")
  print()  
