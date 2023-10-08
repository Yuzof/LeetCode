class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        j = 0
        div = 0
        undiv = 0
        while j <= n:
            if j % m == 0:
                div += j
            else:
                undiv += j
            j += 1
        return undiv - div

A = Solution()
print(A.differenceOfSums(n = 5, m = 1))