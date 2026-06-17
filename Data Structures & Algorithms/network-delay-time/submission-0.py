class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i: [] for i in range(1, n + 1)}
        res = 0
        for u, v, t in times:
            adj_list[u].append((v, t))
        visited = set()
        minHeap = [] 
        heapq.heappush(minHeap, (0, k)) # weight is 0 to start at starting node (trivial)
        weight = 0

        while minHeap:
            weight, start = heapq.heappop(minHeap)
            if start in visited:
                continue
            visited.add(start)
            if len(visited) == n:
                return weight
            for s, w in adj_list[start]:
                heapq.heappush(minHeap, (weight+w, s)) # add previous weight
        return weight if len(visited) == n else -1
        


            
