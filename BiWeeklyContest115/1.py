class Solution(object):
    def lastVisitedIntegers(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        k = 0
        nums = []
        out = []
        for element in words:
            if element == "prev":
                if k >= len(nums):
                    out.append(-1)
                else:
                    out.append(nums[- k - 1])
                k += 1
            else: 
                k = 0
                nums.append(int(element))
        return out
        

A = Solution()
print(A.lastVisitedIntegers(words = ["1","prev","2","prev","prev"]))