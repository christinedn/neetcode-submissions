class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        # push all elements into heap (logn) per insertion
        for s in stones:
            heapq.heappush(max_heap, -1 * s)
        # pop 2 from max heap (ologn time), if equal do not insert back into heap
        while len(max_heap) > 1:
            elem1 = -1 * heapq.heappop(max_heap)
            elem2 = -1 * heapq.heappop(max_heap)
            if elem1 == elem2:
                continue
            # otherwise insert difference into heap 
            heapq.heappush(max_heap, -1*abs(elem1 - elem2))
        return -1 * max_heap[0] if max_heap else 0
        
        