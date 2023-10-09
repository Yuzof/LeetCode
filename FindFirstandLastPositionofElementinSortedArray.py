class Solution:
  def searchRange(self, nums: list[int], target: int) -> list[int]:
      try:
         index = nums.index(target)
      except ValueError:
         return [-1, -1]
      i = index
      while i < len(nums):
          if nums[i] !=  target: break
          i += 1
      return [index, i-1]

A = Solution()
print(A.searchRange(nums = [], target = 0))