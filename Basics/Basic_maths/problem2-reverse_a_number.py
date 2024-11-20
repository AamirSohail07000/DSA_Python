
# Function to reverse a number
def reverseANumber(num):
    ans = 0  # Initialize the reversed number as 0
    while num > 0:  # Continue until all digits are processed
        rem = num % 10  # Extract the last digit of the number
        ans = ans * 10 + rem  # Add the digit to the reversed number in the correct place
        num = num // 10  # Remove the last digit from the number
    return ans  # Return the reversed number

# Input: Read the number from the user
num = int(input("Enter a number to reverse: "))

# Call the function to reverse the number and store the result
ans = reverseANumber(num)

# Output: Print the reversed number
print("Reversed number:", ans)
