# functional parameter
# def pattern (n):
# input from user
# n= int(input("Number of rows :"))
# n=5
# pattern 1
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# n=5
# for i in range (n):
#   for j in range (n):
#     print("*", end=" ")
#   print("") 
# 
# Pattern 2 INCREASING TRIANGLE
# *
# * *
# * * *
# * * * *
# * * * * *

# n= 5
# for i in range(1, n+1):
#   for j in range(i):
#     print('*',end=' ')
#   print()  
#       OR
# n= 5
# for i in range(n):
#   for j in range(i+1):
#     print('*',end=' ')
#   print() 
# 
# Pattern 3 DECREASING PATTERN
# * * * * *
# * * * *
# * * *
# * *
# *  
# n=5
# for i in range(n):
#   for j in range(n-i):
#     print("*", end=" ")
#   print()  

#          OR
# n=5
# for i in range(n):
#   for j in range(i,n):
#     print("*", end=" ")
#   print() 

# Pattern 4 RIGHT SIDED Triangle

# n= 5
# for i in range(n):
#   for j in range(i,n):
#     print(' ',end=' ')  
#   for j in range (i+1):
#     print("*", end=" ")
#   print()    

# Pattern 5 right sided triangle
#  * * * * *
#    * * * *
#      * * *
#        * *
#          *
# Hint- Increasing triangle of space and decreasing triangle of stars
# n=5
# for i in range (n):
#   for j in range (i+1):
#     print(" ", end=" ")
#   for j in range (i,n):
#     print("*", end=" ")
#   print()    

#  Pattern 6 MOUNTAIN Pattern
  #         * 
  #       * * *
  #     * * * * *
  #   * * * * * * *
  # * * * * * * * * *
# Hint- 1 Decreasing triangle of space and two increasing stars where 1 nested loop will print 1 less column
# n= 5
# for i in range (n):
#   for j in range (i,n):
#     print(" ", end=" ")
#   for j in range (2*i+1):
#     print("*", end=" ")  
#   print()  

#   or

# n= 5
# for i in range (n):
#   for j in range (i,n):
#     print(" ", end=" ")
#   for j in range (i):
#     print("*", end=" ") 
#   for j in range (i+1):
#     print("*", end=" ")    
#   print()  

# Pattern 7 REVERSE MOUNTAIN PATTERN

  # * * * * * * * * *
  #   * * * * * * *
  #     * * * * *
  #       * * *
  #         * 
# n= 5
# for i in range (n):
#   for j in range (i+1):
#     print(" ", end=" ")
#   for j in range (i,n-1):
#     print("*", end=" ") 
#   for j in range (i,n):
#     print("*", end=" ")    
#   print()

# Pattern 8 DIAMOND PATTERN
  #         * 
  #       * * *
  #     * * * * *
  #   * * * * * * *
  # * * * * * * * * *
  #   * * * * * * *
  #     * * * * *
  #       * * *
  #         *
# Hint-Run Two mountain pattern code 1 below another
n= 5
for i in range (n-1):
  for j in range (i,n):
    print(" ", end=" ")
  for j in range (i):
    print("*", end=" ") 
  for j in range (i+1):
    print("*", end=" ")    
  print()
for i in range (n):  
  for j in range (i+1):
    print(" ", end=" ")
  for j in range (i,n-1):
    print("*", end=" ") 
  for j in range (i,n):
    print("*", end=" ")    
  print()  