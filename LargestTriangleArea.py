"""
b
|\
| \
|  \
|   \
a----c
"""

# S = |(a[0]*(b[1] - c[1]) + b*(c3-a1) + c*(y1-y2))/2|
"""
class Solution:
    def calc_square(self, a, b, c):
        return abs(a[0]*(b[1] - c[1]) + b[0]*(c[1] - a[1]) + c[0]*(a[1] - b[1]))/2

    def largestTriangleArea(self, points: list[list[int]]) -> float:
        i = 0
        S = 0
        while i < len(points):
            j = i + 1
            while j < len(points):
                k = j + 1
                while k < len(points):
                    if self.calc_square(points[i], points[j], points[k]) > S:
                        a = points[i]
                        b = points[j]   
                        c = points[k]
                        S = self.calc_square(points[i], points[j], points[k])
                    k += 1
                j += 1
            i += 1
        print(a, b, c)
        return self.calc_square(a, b, c)
"""

from itertools import combinations

class Solution:

    def calc_square(self, a, b, c):
        return 0.5*abs(a[0]*(b[1] - c[1]) + b[0]*(c[1] - a[1]) + c[0]*(a[1] - b[1]))
    
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        return max(self.calc_square(a, b, c) for a, b, c in combinations(points, 3))

A = Solution()
print(A.largestTriangleArea(points = [[1,0],[0,0],[0,1]]))