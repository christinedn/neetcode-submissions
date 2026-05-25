class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        start, end = intervals[0]
        for i in range(1, len(intervals), 1):
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            if end >= curr_start:
                end = max(end, curr_end)
            else:
                res.append([start, end])
                start, end = curr_start, curr_end
        res.append([start, end])
        return res


        