import heapq
class MedianFinder:

    def __init__(self):
        # initialize minheap/maxheap
        self.minHeap, self.maxHeap = [], []

    def addNum(self, num: int) -> None:
        # push to min heap
        heapq.heappush(self.minHeap, num)
        if self.maxHeap and self.minHeap[0] < -1 * self.maxHeap[0]:
            elem = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * elem)
        if (len(self.minHeap) - len(self.maxHeap)) > 1:
            elem = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * elem)
        if (len(self.maxHeap) - len(self.minHeap)) > 1:
            elem = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, elem)
        print("minHeap", self.minHeap)
        print("maxHeap", self.maxHeap)
        

    def findMedian(self) -> float:
        # if size is same, pop from both and add those two elements together, and then divide by 2
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + -1 * self.maxHeap[0])/2
        # if size is different, find heap with greater size and return the topmost element
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -1 * self.maxHeap[0]
        
        
        