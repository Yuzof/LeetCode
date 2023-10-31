class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        return [pref[0]] + [pref[i] ^ pref[i-1] for i in range(1, len(pref))]


A = Solution()
#print(A.findArray(pref = [5,2,0,3,1]))
a = int(bin(10), 2)
print(a)  