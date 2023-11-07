class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        dist_len = len(dist)
        arrived = [0]*dist_len
        for i in range(dist_len):
            arrived[i] = (dist[i] / speed[i])
        arrived.sort()
        ans = 0
        for i in range(dist_len):
            if arrived[i] <= i:
                break
            ans += 1
        return ans