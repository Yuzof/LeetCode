class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        for element in s.split():
            ans += element[::-1] + ' '
        return ans[:-1]

A = Solution()
print(A.reverseWords(s = "Let's take LeetCode contest"), 1)