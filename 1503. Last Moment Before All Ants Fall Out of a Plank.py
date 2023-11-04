class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
      return max(set(left + [n - x for x in right]))
                    
A = Solution()
print(A.getLastMoment(n = 4, left = [4,3], right = [0,1]))
print(A.getLastMoment(n = 7, left = [], right = [0,1,2,3,4,5,6,7]))
print(A.getLastMoment(n = 7, left = [0,1,2,3,4,5,6,7], right = []))