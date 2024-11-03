# Print pattern 20
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *
n=5
for i in range (2*n-1):
  # for upper part
  if i<n:
    for j in range (i+1):
      print("*", end="")
    for j in range (2*n-2-2*i):
      print(" ", end="")  
    for j in range (i+1):
      print("*", end="")
  else:
    # For lower part
    # i>=n
    for j in range (2*n-i-1):
      print("*", end="")
    for j in range ((i-n+1)*2):
      print(" ", end="")  
    for j in range (2*n-i-1):
      print("*", end="")              
  print()    