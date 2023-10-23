class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1: return False
        while n >= 1:
            if n % 4 == 0:
                n = n / 4
            else:
                return n == 1
        return False

A = Solution()
for i in range(1000):
  if A.isPowerOfFour(i):
      print(i)