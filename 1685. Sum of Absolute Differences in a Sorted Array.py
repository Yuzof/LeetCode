
"""
class Solution(object):
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        return [sum([abs(i - j) for j in nums]) for i in nums]
"""  
class Solution(object):
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(prefix[-1] + nums[i])
        
        ans = []
        for i in range(len(nums)):
            left_sum = prefix[i] - nums[i]
            right_sum = prefix[-1] - prefix[i]
            
            left_count = i
            right_count = n - 1 - i
            
            left_total = left_count * nums[i] - left_sum
            right_total = right_sum - right_count * nums[i]

            ans.append(left_total + right_total)
        
        return ans  
A = Solution()
print(A.getSumAbsoluteDifferences(nums = [1,4,6,8,10]))