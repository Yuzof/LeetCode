class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        a = set(int(num, 2) for num in nums)
        n = len(nums)
        i = 0 
        while i < n + 1:
            if i not in a:
                ans = bin(i)[2:]
                return "0" * (n - len(ans)) + ans
            i += 1
        return ""
A = Solution()
print(A.findDifferentBinaryString(nums = ["111","011","001"]))