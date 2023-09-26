class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

A = Solution()
print(A.lengthOfLastWord(s = "   fly me   to   the moon  "))