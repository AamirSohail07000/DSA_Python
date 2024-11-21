# A palindrome is a number that reads the same backward as forward. For example, 121, 1331, and 4554 are palindromes because they remain the same when their digits are reversed.


# Function to reverse a number
def reverseANumber(num):
    ans = 0  # Initialize the reversed number as 0
    while num > 0:  # Continue until all digits are processed
        rem = num % 10  # Extract the last digit of the number
        ans = ans * 10 + rem  # Add the digit to the reversed number in the correct place
        num = num // 10  # Remove the last digit from the number
    return ans  # Return the reversed number

def pallindrome(num):
    return num == reverseANumber(num)
# Input: Read the number from the user
num = int(input("Enter a number to reverse: "))


ans = pallindrome(num)

# Output: whether its a pallindrome
print("pallindrome check: ", ans)
