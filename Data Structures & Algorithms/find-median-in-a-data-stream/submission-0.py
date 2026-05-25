class MedianFinder:

    def __init__(self):
        # create small and large heap
        self.small, self.large = [], []
        
    def addNum(self, num: int) -> None:
        # push to small heap (for this algorithm, we are always pushing to small heap first)
        # heapq.heappush(<name_of_list>, <element>)
        # hint: python doesn't let you implement small heaps
        heapq.heappush(self.small, num * -1)

        # make sure every element in small is <= element in large
        if (self.small and self.large and (-1 * self.small[0] > self.large[0])):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # check for uneven size
        # if the difference of the len of heaps is > 1, push to opposite heap
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2
        
        