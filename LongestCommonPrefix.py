class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n = 1
        pref = False
        while n <= len(strs[0]):
            pref = strs[0][:n]
            for element in strs:
                if pref != element[:n]:
                    if n == 1:
                        return ''
                    else:
                        return strs[0][:n-1]
            n += 1 
        return pref if pref else ''

A = Solution()
print(1, A.longestCommonPrefix(strs = ["flower","flow","flight"]))
print(1, A.longestCommonPrefix(strs = ["dog","racecar","car"]))
print(1, A.longestCommonPrefix(strs = ['a']))
print(2, A.longestCommonPrefix(strs = ['']))