from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        l = len(nums)/3
        nums = Counter(nums)
        ans = set()
        for element in nums:
            if nums[element] > l:
                ans.add(element)
        return ans  
    
# numpy .where()???

A = Solution()
print(A.majorityElement(nums = [3, 2 ,3, 3, 4, 4, 4, 4]))