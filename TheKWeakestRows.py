class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        ans = list()
        rows = set()
        i = 0
        while i < len(mat[0]):
          j = 0
          while j < len(mat):
            if mat[j][i] != 1 and j not in rows:
                ans.append(j)
                rows.add(j)
                if len(ans) == k:
                  return ans
            j += 1
          i += 1
        j = 0
        while j < len(mat):
          if j not in rows:
            ans.append(j)
            rows.add(j)
            if len(ans) == k:
              return ans
          j += 1

A = Solution()
print(A.kWeakestRows(mat = 
[[1,1],[1,1],[1,1],[1,1]], 
k = 1))