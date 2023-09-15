class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        paTri = [[1]]
        i = 1
        while i < numRows:
            paTri.append([1,*[paTri[i-1][j-1] + paTri[i-1][j] for j in range(1, len(paTri[i-1]))] , 1])
            i += 1

        return paTri

A = Solution()
print(A.generate(numRows=5))