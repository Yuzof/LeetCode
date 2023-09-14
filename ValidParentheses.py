class Solution(object):
    def isValid(self, s):
        valid = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:
            if bracket in pairs:
                valid.append(bracket)
            elif len(valid) == 0 or bracket != pairs[valid.pop()]:
                return False
        return len(valid) == 0

A = Solution()

print(A.isValid("[([]])"))
print(A.isValid("([)]"))
print(A.isValid("{[]}"))
print(A.isValid("["))