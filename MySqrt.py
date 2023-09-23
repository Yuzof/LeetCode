class Solution:
    def mySqrt(self, x: int) -> int:
        if (x >= 536_848_900 - 1):
          if (x >= 1_207_910_025):
            i = 34_754
          else:
            i = 23_169 
        elif (x >= 134_212_225):
           i = 11_584
        else:
           i = 0
        while(i * i <= x):
            i += 1
        return i - 1 

A = Solution()
print(A.mySqrt(100))