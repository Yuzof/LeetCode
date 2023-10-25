"""
import copy

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ans = [0]
        i = 0
        while i < n - 1:
            tmp = copy.deepcopy(ans)
            _len = 2**i
            ans = [0]*_len * 2
            for j in range(_len):
                if tmp[j] == 0:
                    ans[2*j + 1] = 1
                else:
                    ans[2*j] = 1
            i += 1
        return ans[k-1]
"""

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        length = 2 ** (n - 2)
        if k <= length:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - length)

A = Solution()
print(A.kthGrammar(n = 3, k = 1))