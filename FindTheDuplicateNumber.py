class Solution:
  def findDuplicate(self, nums: list[int]) -> int:
    seen = set()
    i = 0
    while i < len(nums):
      if nums[i] not in seen:
        seen.add(nums[i])
      else:
        return nums[i]
      i += 1

A = Solution()
print(A.findDuplicate(nums = [1,3,4,2,2]))