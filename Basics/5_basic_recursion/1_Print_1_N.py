# Given an integer n, write a function to print all numbers from 1 to n (inclusive) using recursion.

# You must not use any loops such as for, while, or do-while.
# The function should print each number on a separate line, in increasing order from 1 to n.
# Note:
# Recursion means a function calls itself until a base condition is reached.

# To print numbers from 1 to n without loops, we use recursion in a way that:

# The function first recursively calls itself for smaller numbers.

# Then, after coming back from recursion, it prints the current number.

# This naturally gives us numbers in increasing order.
class Solution:
    def printNumbers(self, n):
        # Base case
        if n == 0:
            return
        
        # Recursive call: first print numbers from 1 to n-1
        self.printNumbers(n-1)

        # After returning from recursion, print current number
        print(n)
# Example usage
n = 5
print(f"Printing numbers from 1 to {n} using recursion:")
# Create object of Solution class
obj = Solution()
obj.printNumbers(n)