# Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion

class Solution:
  def NnumbersSum(self, N):
      """
      Recursive function to calculate sum of first N natural numbers.
      """

      # Base case: when N becomes 0, return 0
      if N == 0:
          return 0

      # Recursive case: add current N and call for N-1
      return N + self.NnumbersSum(N - 1)


# Example usage
N = 10
obj = Solution()   # Create object of class
print(f"Sum of first {N} natural numbers is:", obj.NnumbersSum(N))


  
