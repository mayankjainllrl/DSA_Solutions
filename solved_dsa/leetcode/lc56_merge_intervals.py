class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result_intervals = []
        
        for interval in intervals:
            flag = 0
            for i, result_interval in enumerate(result_intervals):
                if interval[0] <= result_interval[1] <= interval[1] or result_interval[0] <= interval[1] <= result_interval[1]:
                    result_intervals[i] = [min(interval[0], result_interval[0]), max(interval[1], result_interval[1])]
                    flag = 1
                    break
            print(result_intervals)
            if not flag:
                result_intervals.append(interval)
        
        return result_intervals
                
    
intervals = [[9, 10], [6, 8], [3, 5], [7, 10]]
print(Solution().merge(intervals))