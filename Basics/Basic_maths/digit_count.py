# count no of digits in a number
# def countNumber(num):
#     return len(str(abs(num))) # Use abs() to ignore the negative sign


# num = int(input("Enter a number : "))
# result = countNumber(num)
# print(result)

#     OR
        # BRUTE FORCE APPROACH
# Function to count the number
# of digits in an integer 'n'

def countDigits(n):
    cnt = 0
    while n > 0:
        # Increment the counter for each digit encounter
        cnt = cnt + 1
        # Divide 'n' by 10 to remove the last digit.
        n = n // 10
    # return the count of digits
    return cnt 

if __name__ == "__main__":
    # N = 436789
    N = int(input("Enter a number: "))
    print("N: ", N)
    digits = countDigits(N)
    print("Number of digits in N: ", digits)


# G4G Question
# Given a number n. Count the number of digits in n which evenly divide n. Return an integer, total number of digits of n which divides n evenly.

# Note :- Evenly divides means whether n is divisible by a digit i.e. leaves a remainder 0 when divided.

# def countNum(num):
#     return len(str(abs(num))) # Use abs() to ignore the negative sign
  