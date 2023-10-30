class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

A = Solution()
print(A.sortByBits(arr = [0,1,2,3,4,5,6,7,8]))