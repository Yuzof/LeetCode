class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = sorted(list(set(nums)))[:]
        return len(nums)


nums = [1,1,2]
A = Solution()
print(A.removeDuplicates(nums = nums))
print(nums)