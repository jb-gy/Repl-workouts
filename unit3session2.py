class Solution:
  def __init__(self):
      self.seen = {}
  def isHappy(self, n: int) -> bool:
      # Start with the given number.
      # Compute the sum of squares of its digits.
      sum = 0
      for digit in str(n):
          sum = sum + int(digit) ** 2
      # If the result is 1, return true (the number is happy).
      print(sum)
      if sum == 1:
          return True
      # If the result has been seen before (i.e., it is already in the HashSet), return false (indicating the presence of a cycle).
      if sum in self.seen:
          return False
      else:
          self.seen[sum] = True
      # Otherwise, update the number to the computed result 
      # and repeat the process.
      return self.isHappy(sum)