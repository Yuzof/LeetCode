import time
class Solution(object):
    def isMatch(self, s:str, p:str) -> bool:
        # Как только закончили рекурсию
        if not p: return not s # Если нет больше шаблона, то если и текста нет, то все хорошо
        # Выражение не закончено, есть еще буквы?
        # Если нет, то может стоит .*?
        match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*': # если не выполнено, тогда не попали
            return (self.isMatch(s, p[2:]) or # буквально либо 0 повторений символа (или все повторения уже учтены)
                    match and self.isMatch(s[1:], p)) # либо сколько угодно пока не доехали до конца
        else:
            return match and self.isMatch(s[1:], p[1:]) # либо без звездочки просто учли символ

A = Solution()
print('F', A.isMatch(s = "a", p = "a"))
print('F', A.isMatch(s = "aaa", p = "aaaa"))
print('T', A.isMatch(s = "a", p = "ab*"))
print('F', A.isMatch(s = "a", p = "ab*a"))
print('T', A.isMatch(s = "aaa", p = "a*a"))
print('T', A.isMatch(s = "aaa", p = "ab*a*c*a"))
start = time.time()
result = A.isMatch(s = "aaaaaaaaaaaaaaaaaaa", p = "a*a*a*a*a*a*a*a*a*b")
print(result, time.time() - start)