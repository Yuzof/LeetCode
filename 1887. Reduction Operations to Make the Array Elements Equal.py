class Solution(object):
    def reductionOperations(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        ans = 0
        while i < len(nums) - 1:
            if nums[i] > nums[i+1]:
                ans += i + 1
            i += 1
        return ans

A = Solution()
print(A.reductionOperations(nums = [5,1,3]))