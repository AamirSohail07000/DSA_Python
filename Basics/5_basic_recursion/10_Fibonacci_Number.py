# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,



# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.


# Given n, calculate F(n).

class Solution:
    def fibonacci(self, n):
        """
        Recursive function to return nth Fibonacci number.
        Formula: F(n) = F(n-1) + F(n-2)
        """

        # Base Cases
        if n == 0:
            return 0
        if n == 1:
            return 1

        # Recursive case:
        # For n > 1, return sum of previous two Fibonacci numbers
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)


# Example usage
obj = Solution()
n = 9
print(f"Fibonacci number at position {n} is:", obj.fibonacci(n))

