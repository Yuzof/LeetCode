class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        i = 2
        while i <= n:
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
            i += 1
        return dp[n]

A = Solution()
print(A.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))