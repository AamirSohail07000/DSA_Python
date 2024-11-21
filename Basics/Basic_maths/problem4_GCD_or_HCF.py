def gcd(a,b):
  divisor = min(a,b)
  dividend = max(a,b)

  while dividend % divisor !=0:
    temp = dividend
    dividend = divisor
    divisor = temp % divisor
  return divisor
a = int(input("Insert Value for a : "))
b = int(input("Insert Value for b : "))
ans = gcd(a,b)
print("HCF of a and b is : ",ans)  