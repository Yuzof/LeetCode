import numpy as np

class Solution(object):
    def calc_len(self, w1, w2):
        diff = 0
        for i in range(min(len(w1), len(w2))):
            if w1[i] != w2[i]:
                diff += 1
        return diff + abs(len(w1) - len(w2))*2

    def getWordsInLongestSubsequence(self, n, words, groups):
        """
        :type n: int
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        i = 0
        ans = []
        while i <= n:
            if groups

A = Solution()

print(A.getWordsInLongestSubsequence(n = 6, words = ["aab","cab","ba","dba","daa","bca"], groups = [4,3,4,6,4,3]))
print(A.getWordsInLongestSubsequence(n = 3, words = ["ccd","bb","ccc"], groups = [1,1,2]))
print(A.getWordsInLongestSubsequence(n = 1, words = ["abbbb"], groups = [1]))
print(A.getWordsInLongestSubsequence(n = 3, words = ["bab","dab","cab"], groups = [1,2,2]))
print(A.getWordsInLongestSubsequence(n = 4, words = ["a","b","c","d"], groups = [1,2,3,4]))
print(A.getWordsInLongestSubsequence(n = 3, words = ["bdb","aaa","ada"], groups = [2,1, 3]))