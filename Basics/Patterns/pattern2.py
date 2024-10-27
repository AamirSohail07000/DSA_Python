# Pattern 2
# *
# * *
# * * *
# * * * *
# * * * * *
# n = int(input("Enter the value of N: "))
n=5
for i in range (n):
  for j in range(i+1):
    print("*", end=" ")
  print("")  