# Print pattern 17
#     A
#    ABA
#   ABCBA
#  ABCDCBA

n=4
def numToChr(num):
  return chr(num+65)
for i in range(n):
  for j in range(n-i):
    print(" ",end="")
  for j in range(i+1):
    print(numToChr(j), end="")
  for j in range(1,i+1):
    print(numToChr(i-j), end="")  
  print()    