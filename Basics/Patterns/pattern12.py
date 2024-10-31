# 1      1
# 12    21
# 123  321
# 12344321

n=5
for i in range (1,n):
  for j in range(1,i+1):
    print(j,end="")
  for j in range (i,n-1):
    print(" ",end="")
  for j in range (i,n-1):
    print(" ",end="")
  for j in range(1,i+1):
    print(i-j+1,end="")
  print()      