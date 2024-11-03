# print pattern 19
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

# Method 1
# n=5
# for i in range(n):
#   for j in range(n-i):
#     print("*", end="")
#   for j in range(1,i+1):
#     print(" ",end="")  
#   for j in range(1,i+1):
#     print(" ",end="")
#   for j in range(n-i):
#     print("*", end="")       
#   print() 
# for i in range(n):
#   for j in range(i+1):
#     print("*", end="")
#   for j in range(1,n-i):
#     print(" ",end="")  
#   for j in range(1,n-i):
#     print(" ",end="")
#   for j in range(i+1):
#     print("*", end="")       
#   print() 




# Method 2
n= 5
for i in range (2*n):
  
  if i<n:
    # For upper part
    for j in range(n-i):
      print("*", end="")
    for j in range (2*i):
      print(" ", end="")
    for j in range(n-i):
      print("*", end="")
  else:
    # For upper part
    # i>=n  
    for j in range(i-n+1):
      print("*", end="")
    for j in range ((2*n-i-1)*2):
      print(" ", end="")
    for j in range(i-n+1):
      print("*", end="")                
  print()  