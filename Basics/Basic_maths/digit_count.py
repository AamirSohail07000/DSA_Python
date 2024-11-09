
# def countNumber(num):
#     return len(str(abs(num))) # Use abs() to ignore the negative sign


# num = int(input("Enter a number : "))
# result = countNumber(num)
# print(result)

# G4G Question
# Given a number n. Count the number of digits in n which evenly divide n. Return an integer, total number of digits of n which divides n evenly.

# Note :- Evenly divides means whether n is divisible by a digit i.e. leaves a remainder 0 when divided.

def countNum(num):
    return len(str(abs(num))) # Use abs() to ignore the negative sign
  