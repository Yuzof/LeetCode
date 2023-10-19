class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def parse(w: str):
            ans = ''
            for element in w:
                if element != '#':
                    ans += element
                elif len(ans) > 0:
                    ans = ans[0:-1:1]
            return ans
        print(parse(s), parse(t))
        return parse(s) == parse(t)

A = Solution()
print(A.backspaceCompare(s = "a#c", t = "b"))