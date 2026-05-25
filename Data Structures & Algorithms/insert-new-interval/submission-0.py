class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        ind = 0
        start, end = newInterval[0], newInterval[1]
        while ind < len(intervals) and intervals[ind][1] < start:
            res.append(intervals[ind])
            ind += 1
        # is it guaranteed that there is overlap at this point? no!!! 
        # now we have to find the ending interval
        while ind < len(intervals) and end >= intervals[ind][0]:
            start = min(intervals[ind][0], start)
            end = max(intervals[ind][1], end)
            ind += 1
        res.append([start, end])
        # append the rest
        while ind < len(intervals):
            res.append(intervals[ind])
            ind += 1
        return res

            
            