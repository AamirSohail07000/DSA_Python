# Check if a number is prime or not


# Problem Statement: Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.

# Approach 1
# We can iterate through numbers from 1 to n, counting how many of these numbers divide n without a remainder. If exactly two numbers do, so n is prime otherwise it is not prime.

# Algorithm:

# Step 1:Initialise a variable cnt to count the number of factors and set it to 0.

# Step 2:Start a loop from 1 to n, iterating through each number i. Inside the loop:

# Check if n is divisible by i without any remainder.
# If it is, increment the counter variable by 1.
# Step 3:After the loop if the number of divisors is equal to 2, return true indicating the number is prime.

# If the number of divisors is not equal to 2 (but greater), return false indicating that the number is not prime.

# Function to check if a
# given number is prime.
# def checkPrime(n):
#     # Initialize a counter variable to
#     # count the number of factors.
#     cnt = 0
#     # Loop through numbers from 1 to n.
#     for i in range(1, n+1):
#         # If n is divisible by i
#         # without any remainder.
#         if n % i == 0:
#             # Increment the counter.
#             cnt = cnt + 1

#     # If the number of
#     # factors is exactly 2
#     if cnt == 2:
#         # Return True, indicating
#         # that the number is prime.
#         return True
#     # If the number of
#     # factors is not 2.
#     else:
#         # Return False, indicating
#         # that the number is not prime.
#         return False

# if __name__ == "__main__":
#     n = 1483
#     isPrime = checkPrime(n)
#     if isPrime:
#         print(n, "is a prime number.")
#     else:
#         print(n, "is not a prime number.")


# Approach 2
# Optimal approach

import math

# Function to check if a
# given number is prime.
def checkPrime(n):
    # Initialize a counter variable to
    # count the number of factors.
    cnt = 0

    # Loop through numbers from 1
    # to the square root of n.
    for i in range(1, int(math.sqrt(n)) + 1):
        # If n is divisible by i
        # without any remainder.
        if n % i == 0:
            # Increment the counter.
            cnt = cnt + 1

            # If n is not a perfect square,
            # count its reciprocal factor.
            if n // i != i:
                cnt = cnt + 1

    # If the number of
    # factors is exactly 2.
    if cnt == 2:
         # Return true, indicating
         # that the number is prime.
        return True
    # If the number of
    # factors is not 2.
    else: 
        # Return false, indicating
        # that the number is not prime.
        return False

# Main function
def main():
    n = 1483
    isPrime = checkPrime(n)
    if isPrime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")

if __name__ == "__main__":
    main()