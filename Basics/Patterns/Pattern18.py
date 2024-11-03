# Print pattern 18
# E
# DE
# CDE
# BCDE
# ABCDE
n= 5
def numToChr(num):
  return chr(69-num)
for i in range (n):
  for j in range(i+1):
    print(numToChr(i-j),end="")
  print()  