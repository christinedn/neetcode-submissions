class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        res = 0
        for i in range(1, len(intervals), 1):
            if intervals[i][0] < end: # overlap
                # remove that interval
                res += 1
            else:
                # no overlap, keep the interval, update end
                end = max(end, intervals[i][1])
        return res
