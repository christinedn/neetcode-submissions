"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        minheap = []
        for i in intervals:
            if minheap and minheap[0] <= i.start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, i.end)
        return len(minheap)

