import itertools
import copy

class Solution:    
    def distributeCandies(self, n: int, limit: int) -> int:
        cout = 0
        for i in range(min(n, limit) + 1):
            for j in range(min(n, limit) + 1):
                k = (n - j - i)
                if 0 <= k <= limit:
                    cout += 1
        return cout
A = Solution()
print(A.distributeCandies(n = 5, limit = 2))