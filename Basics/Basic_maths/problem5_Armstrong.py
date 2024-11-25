# An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
# For example, if you have a number like 153, it's an Armstrong number because 1^3 + 5^3 + 3^3 equals 153.(Digit=3 so power would be 3 like 1^3)

# Step 1:Calculate the number of digits in the input number and store it in k.

# Step 2: Initialise a variable sum to 0. This variable will store the sum of each digit raised to the power of number of digits in number.

# Make a copy of the original number to store it in a temporary variable.
# Step 3: Run a while loop with the condition n>0 and at each iteration:

# Get the last digit of n by using the modulus operator % with 10 and store it in a temporary variable ld.
# Add the digit ld raised to the power of k of the sum.
# Update n by integer division with 10 effectively removing the last digit.
# Step 4: After the loop, check if the original input number is equal to the sum of the digits raised to the power of the number of digits in the number.

# If they are equal, return true indicating the number is an Armstrong number.
# If they are not equal, return false indicating that the number is not an Armstrong number.



# Function to check if a number is an Armstrong number
def isArmstrong(num):
    # Convert the number to a string to count the number of digits
    # For example, if num = 153, then len(str(153)) = 3
    k = len(str(num))  
    
    # Initialize a variable to hold the sum of the digits raised
    # to the power of the number of digits (k)
    sum = 0  
    
    # Create a copy of the input number to use in calculations
    # This ensures the original number remains unchanged
    n = num  
    
    # Loop to process each digit of the number
    while n > 0:  
        # Extract the last digit of the number using modulo operator(used to find remainder)
        # For example, if n = 153, then ld = 153 % 10 = 3
        ld = n % 10  
        
        # Raise the digit to the power of k (number of digits)
        # and add it to the sum
        # For example, if ld = 3 and k = 3, then sum += 3 ** 3 = 27
        sum += ld ** k  
        
        # Remove the last digit from the number using integer division
        # For example, if n = 153, then n = 153 // 10 = 15
        n = n // 10  
    
    # After processing all digits, check if the calculated sum equals
    # the original number. If it does, the number is an Armstrong number.
    return sum == num

def main():
    number = 153
    if isArmstrong(number):
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")

if __name__ == "__main__":
    main()