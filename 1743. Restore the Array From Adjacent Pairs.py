from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        adjs = defaultdict(set)
        for i, j in adjacentPairs:
            adjs[i].add(j)
            adjs[j].add(i)
        for node, adj in adjs.items():
            if len(adj) == 1:
                break
        ans=[node]
        while adjs[node]:
            new = adjs[node].pop()
            ans.append(new)
            adjs[new].remove(node)
            node = new
        return ans   

A = Solution()
print(A.restoreArray(adjacentPairs=[[2, 1],[3, 4],[3, 2]]))