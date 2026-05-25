# max (min) heap: the element at the root is greater than all children
# min (max) heap: the element at the root is smaller than all children
# always push to min heap
# after pushing, check if the difference in len is greater than 1
    # if greater than, move to max heap until difference in length is equal to or less than 1

# find median: check size of heap
# if size is equal, add the roots and divide by two. return that result
# if size are not equal, this means that the median will be the root of max heap
class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # must negate the number bc python has no native max heap
        self.minHeap = []
    
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -1 * (num))
        while len(self.maxHeap) - len(self.minHeap) > 1:
            elem = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, elem)
        if len(self.minHeap) != 0:
            elem1 = -1 * self.maxHeap[0]
            elem2 = self.minHeap[0]
            if elem1 > elem2:
                swap1 = -1 * heapq.heappop(self.maxHeap)
                swap2 = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -1 * swap2)
                heapq.heappush(self.minHeap, swap1)
                
    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            print("here")
            return (-1 * self.maxHeap[0] + self.minHeap[0])/2
        else:
            print("here2")
            return -1 * self.maxHeap[0]
        
        