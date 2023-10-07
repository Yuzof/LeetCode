class Solution:
    def __init__(self):
        self.mod = 10**9 + 7

    def find_max(self, arr: list[int]) -> int:
        maximum_value = -1
        maximum_index = -1
        search_cost = 0
        n = len(arr)
        for i in range(n):
            if (maximum_value < arr[i]):
                maximum_value = arr[i]
                maximum_index = i
                search_cost += 1
        return maximum_index
    
    def helper(self, indx, curr_max, cost, m, dp):
        tpl = (indx, curr_max, cost)
        if tpl in dp:
            return dp[tpl]
        if indx == 1:
            return 1 if cost == 1 else 0
        numberWays = 0
        j = 1
        while j <= m:
            if j <= curr_max:
                numberWays += self.helper(indx-1, curr_max, cost, m, dp)
            else:
                numberWays += self.helper(indx-1, j, cost-1, m, dp)
            j += 1
        dp[tpl] = numberWays % self.mod
        return dp[tpl]

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        ans = 0
        dp = {}
        i = 1
        while i <= m:
            ans = (ans + self.helper(n, i, k, m, dp)) % self.mod
            i += 1
        return ans

A = Solution()
print(A.numOfArrays(n = 2, m = 3, k = 1))