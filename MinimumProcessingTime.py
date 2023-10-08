class Solution:
    def minProcessingTime(self, processorTime: list[int], tasks: list[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        t_out = 0
        i =  0
        while i < len(processorTime):
            calc_time = (processorTime[i] + max(tasks[4*i], tasks[4*i + 1], tasks[4*i + 2], tasks[4*i + 3]))
            if calc_time >= t_out:
                t_out = calc_time
            i += 1
        return t_out

A = Solution()
print(A.minProcessingTime(processorTime = [10,20], tasks = [2,3,1,2,5,8,4,3]))