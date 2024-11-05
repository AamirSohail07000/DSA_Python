# print pattern 21
# ****
# *  *
# *  *
# ****

# Method 1
# n = 5
# for i in range(1,n):
#   if i==1 or i==4:
#     for j in range(1,n):
#       print("*", end="")
#   else:
#     for j in range(n-4):
#       print("*", end="")
#     for j in range(3,n):
#       print(" ", end="")
#     for j in range(n,n+1):
#       print("*", end="")        
#   print() 

#  Method 2
# n=4
# for i in range(n):
#   for j in range(n):
#     if i==0 or i==n-1 or j==0 or j==n-1:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()    
