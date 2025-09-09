# Given an integer n, write a function to print all numbers from n to 1 (inclusive) using recursion.

# You must not use any loops such as for, while, or do-while.
# The function should print each number on a separate line, in decreasing order from n to 1

class Solution:
    def printNumbers(self, n):
        # Base case
        if n == 0:
            return

        # Print current number first
        print(n)

        # Recursive call for smaller number
        self.printNumbers(n-1)

# Example usage
n = 5
print(f"Printing numbers from {n} to 1 using recursion:")
# Create object of Solution class
obj = Solution()
obj.printNumbers(n)