# Weekly Contest 366 Task 3
# Not Solved

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        s1 = list(s1)
        s2 = list(s2)
        if s1.count('1') % 2 != s2.count('1') % 2:
            return -1
        def flip(i:int , j:int) -> None:
            if s1[i] == '1': s1[i] = '0' 
            else: s1[i] = '1'
            if s1[j] == '1': s1[j] = '0'
            else: s1[j] = '1'
        i = 0
        score = 0
        str_len = len(s1)
        while i < str_len - 1:
            if s1[i] != s2[i] and s1[i+1] != s2[i+1]:
                  score += 1
                  flip(i, i+1)
                  i += 1
            i += 1
        i = 0
        while i < str_len:
            if s1[i] != s2[i]:
                j = i + 1
                while j < str_len - 1:
                    if s1[j] != s2[j]:
                      break
                    else:
                        j += 1
                if j - i < x:
                    score += j - i
                else:
                    score += x
                flip(i, j)
            i += 1
        return score

A = Solution()
print(4, A.minOperations(s1 = "11001011111", s2 = "01111000110", x = 2))
print(4, A.minOperations(s1 = "1100011000", s2 = "0101001010", x = 2))
print(-1, A.minOperations(s1 = "10110", s2 = "00011", x = 4))
