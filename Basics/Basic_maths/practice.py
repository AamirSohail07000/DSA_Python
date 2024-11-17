# N = 7789
# digit1= N % 10
# digit2=int(N/10)%10
# digit3=int(N/100)%10
# digit4=int(N/1000)%10
# print(digit1)
# print(digit2)
# print(digit3)
# print(digit4)


# OPTIMAL APPROACH
import math

# Calculate the count of digits in 'n'
# using logarithmic operation log10(n) + 1.
def countDigits(n):
    # Initialize a variable 'cnt' to
    # store the count of digits.
    cnt = int(math.log10(n) + 1)

    # The expression int(math.log10(n) + 1)
    # calculates the number of digits in 'n'
    # and casts it to an integer.
    
    # Adding 1 to the result accounts
    # for the case when 'n' is a power of 10,
    # ensuring that the count is correct.
   
    # Finally, the result is cast
    # to an integer to ensure it is rounded
    # down to the nearest whole number.
    
    # Return the count of digits in 'n'.
    return cnt
# Main function
if __name__ == "__main__":
    # N = 329823
    N = int(input("Enter a Number: "))
    print("N:", N)
    digits = countDigits(N)
    print("Number of Digits in N:", digits)

# G4G Question
# Given a number n. Count the number of digits in n which evenly divide n. Return an integer, total number of digits of n which divides n evenly.

# Note :- Evenly divides means whether n is divisible by a digit i.e. leaves a remainder 0 when divided.

# def countNum(num):
#     return len(str(abs(num))) # Use abs() to ignore the negative sign
  