# Print pattern 16
# A
# BB
# CCC
# DDDD
# EEEEE


n=5
def numToChr(num):
  return chr(num+65)
for i in range(n):
  for j in range(i+1):
    print(numToChr(i),end="")
  print()  