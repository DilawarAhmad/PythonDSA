class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: (x[0], -x[1]))
        prev = intervals[0]
        count = 0
        for i in range(1,len(intervals)):
            curr = intervals[i]
            if curr[0] >= prev[0] and curr[1] <= prev[1]:
                count+=1
            else:
                prev = curr
        return len(intervals) - count
