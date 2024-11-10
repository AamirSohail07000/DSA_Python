# Problem statement
# You are given a number ’n’.



# Find the number of digits of ‘n’ that evenly divide ‘n’.



# Note:
# A digit evenly divides ‘n’ if it leaves no remainder when dividing ‘n’.


# Example:
# Input: ‘n’ = 336

# Output: 3

# Explanation:
# 336 is divisible by both ‘3’ and ‘6’. Since ‘3’ occurs twice it is counted two times.
# Note:
# You don’t need to print anything. Just implement the given function.


# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 35


# Sample Output 1:
# 1


# Explanation of sample output 1:
# 35 is only divisible by ‘5’, hence answer is 1.


# Sample Input 2:
# 373


# Sample Output 2:
# 0


# Explanation of sample output 2:
# There’s no digit in 373 that evenly divides it. Hence the output is 0.


# Expected Time Complexity:
# Try to solve this in O(log(n)) 


# Constraints:
# 1 <= ‘n’ <= 10^9

# Time Limit: 1 sec

# Solution

n = int(input("Enter a number: "))

def countDigits(n):
    cnt = 0  # Define cnt inside the function
    original_n = n  # Store the original value of n for modulo operations

    while n > 0:
        lastDigit = n % 10
        n = n // 10  # Use integer division to remove the last digit
        # Check if lastDigit is not zero and divides the original number
        if lastDigit != 0 and original_n % lastDigit == 0:
            cnt += 1  # Increment cnt if condition is met
    return cnt

# Call the function and print the result
print("Count of digits that evenly divide n:", countDigits(n))

   
