class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        res = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(min_heap, (dist, [x,y]))
        for i in range(k):
            elem = heapq.heappop(min_heap)
            res.append(elem[1])
        return res