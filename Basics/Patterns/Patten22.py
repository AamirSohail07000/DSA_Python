# print pattern 22
# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444


n= 4
for i in range(2*n-1):
    for j in range(2*n-1):
      row = min(i,2*n-2-i)
      col = min(j,2*n-2-j)
      ans= min(row,col)
      print(4-ans, end="")
    print()  