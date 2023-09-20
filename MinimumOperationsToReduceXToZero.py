# How we think about a solution - O(n) time, O(1) space - Python, JavaScript, Java, C++
# Лучше, чем рекурсия. Интересная идея, что можно смотреть не число, а target + x = sum(nums)

"""
class Solution:
  def minOperations(self, nums: list[int], x: int, i: int = 1) -> int:
    if sum(nums) < x:
      return -1
    if nums and x > 0:
      if (nums[0] == x or nums[-1] == x):
        return i
      else:
        try:
          return min(p for p in (self.minOperations(nums = nums[1:], x = x-nums[0], i  = i + 1), self.minOperations(nums = nums[0:-1], x = x-nums[-1], i  = i + 1)) if p > 0)
        except ValueError:
          return -1
    else:
      return -1
"""
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        left = 0
        cur_sum = 0
        max_sub_length = float('-inf')
        n = len(nums)
        for right in range(n):
            cur_sum += nums[right]
            while cur_sum > target:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                max_sub_length = max(max_sub_length, right - left + 1)
        return -1 if max_sub_length == float('-inf') else n - max_sub_length

A = Solution()
print(A.minOperations([6285,2511,3617,8040,6970,8187,5617,7665,5069,875,3570,378,6556,1147,8616,3140,561,2875,5087,1372,2617,756,9076,1381,5428,498,1386,6984,5624,7908,5724,9921,4368,7036,92,4584,2654,2942,9947,9832,9969,9965,9991,9999,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,9992,10000,9985,8145,8244,4960,7560,7757,3981,8841,3482,2188,3475,1594,5101,4404,9679,3500,6984,5108,7258,9696,702,9031,2502,2326,5099,4767,7164,9432,2084,5294,7382,7564,809], x = 842910))
