class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        return max([nums[i] + nums[-i - 1] for i in range(len(nums) // 2)])

A = Solution()
print(A.minPairSum(nums = [3,5,4,2,4,6]))