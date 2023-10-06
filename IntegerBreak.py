import math

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n - 1
        ans = [3] * (n // 3)
        if n % 3 == 2:
            ans.append(2)
        elif n % 3 == 1:
            ans[0] = 4
        return math.prod(ans)

A = Solution()
print(A.integerBreak(n = 5))
        