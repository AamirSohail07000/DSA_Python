# Approach 1
# A brute force approach would be to iterate from 1 to n checking each value if it divides n without leaving a remainder. For each divisor found, store it in an array and a count of divisors is maintained. After iterating through all possible values, the size of the array is updated with the count of divisors and the array is returned.

# Algorithm:

# Step 1:Initialise an array to store the divisors.

# Step 2:Iterate from 1 to n using a loop variable ‘i’. For each value of ‘i’:

# Check if ‘i’ is a divisor of ‘n’ by checking if ‘n’ is divisible by ‘i’ without a remainder (‘n’%i == 0).
# If i is a divisor, store it in the


# def numDivisors(num):
#   for i in range(1,num+1):
#     if num%i==0:
#       print(i)
    
# numDivisors(28)

# OPTIMAL APPROACH
import math

# Function to find all divisors of a given number `n`
def findDivisors(n):
    # Initialize an empty list to store the divisors of the number
    divisors = [] 

    # Calculate the square root of the number `n`
    # We'll use this as the upper limit for our iteration
    sqrtN = int(math.sqrt(n)) 
    
    # Loop through numbers from 1 to the square root of `n` (inclusive)
    # This helps to find all divisors efficiently
    for i in range(1, sqrtN + 1): 
        # Check if `i` is a divisor of `n`
        # If dividing `n` by `i` leaves no remainder, then `i` is a divisor
        if n % i == 0: 
            # Add `i` (the current divisor) to the list
            divisors.append(i) 

            # Add the counterpart divisor `n // i` to the list
            # `n // i` is another divisor of `n` that corresponds to `i`
            # For example, if `n = 12` and `i = 2`, then `n // i = 6` is also a divisor
            # Ensure we don't add the same divisor twice (e.g., when `i` is the square root of `n`)
            if i != n // i:
                divisors.append(n // i) 
    
    # Return the complete list of divisors
    return divisors 

# Main block to execute the program
if __name__ == "__main__":
    # Define the number for which we want to find divisors
    number = 34

    # Call the `findDivisors` function and store the result in a variable
    divisors = findDivisors(number)

    # Print the divisors in a formatted way
    print("Divisors of", number, "are:", end=" ")
    for divisor in divisors:
        print(divisor, end=" ")
    print()



# Complexity Analysis

# Time Complexity: O(sqrt(N)) where N is the input number. The algorithm iterates through each number from 1 to the square root of N once to check if it is a divisor.

# Space Complexity : O(2*sqrt(N))where N is the input number. This approach allocates memory for an array to hold all the divisors. The size of this array could go to be 2*(sqrt(N)).

