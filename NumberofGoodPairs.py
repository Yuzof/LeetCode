class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        i = 0
        cnt = 0
        while i < len(nums)-1:
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    cnt += 1
                j += 1
            i += 1
        return cnt

A = Solution()
print(A.numIdenticalPairs(nums = [1,2,3]))