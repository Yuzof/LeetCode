class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            t = target - nums[i]
            for j in range(i+1, len(nums)):
                count += 1 if nums[j] < t else 0
        return count

A = Solution()
print(A.countPairs(nums = [-6,2,5,-2,-7,-1,3], target = -2))