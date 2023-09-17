class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums

A = Solution()
print(A.getConcatenation(nums = [1,3,2,1]))