import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap, self.maxHeap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)

        while self.maxHeap and self.maxHeap[0] * -1 > self.minHeap[0]:
            elem = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, elem * -1)
        # rebalance
        if (len(self.minHeap) - len(self.maxHeap)) > 1:
            elem = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, elem*-1)

        if (len(self.maxHeap) - len(self.minHeap)) > 1:
            elem = heapq.heappop(self.maxHeap) * -1
            heapq.heappush(self.minHeap, elem)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0]+(-1 * self.maxHeap[0]))/2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -1 * self.maxHeap[0]
        
        
        