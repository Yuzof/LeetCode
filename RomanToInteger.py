class Solution:
    def __init__(self):
        self.roman_alphabet_combinations = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        self.roman_alphabet = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    def romanToInt(self, s: str) -> int:
        num, i =  0, 0
        while i < len(s):
            try:
                if (s[i] + s[i+1]) in self.roman_alphabet_combinations:
                    num += self.roman_alphabet_combinations[s[i] + s[i+1]]
                    i += 2
                else:
                    num += self.roman_alphabet[s[i]]
                    i += 1
            except IndexError:
                num += self.roman_alphabet[s[i]]
                i += 1
        return num

A = Solution()
print(A.romanToInt("MCMXCIV"))