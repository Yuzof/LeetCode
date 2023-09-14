class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        for i in range(len(x_str)//2):
            if x_str[i] == x_str[-i-1]:
                continue
            else:
                return False
        return True

A = Solution()
print(A.isPalindrome(10))