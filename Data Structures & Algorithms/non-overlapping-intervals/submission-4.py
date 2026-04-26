class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        print(intervals)
        # sort by the second index
        res = 0
        end = intervals[0][1]
        # compare end with the starting of ith interval
        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                # overlap
                res += 1
            else: # new end
                end = intervals[i][1]
        return res
