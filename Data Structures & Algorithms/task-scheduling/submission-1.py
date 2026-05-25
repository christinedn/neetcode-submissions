class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-freq for freq in count.values()] 
        heapq.heapify(max_heap)

        q = deque()
        time = 0
        while max_heap or q:
            time += 1
            if max_heap:
                curr_task_amt = heapq.heappop(max_heap)
            curr_task_amt += 1
            time_can_process = time + n
            if curr_task_amt < 0:
                q.append([curr_task_amt, time_can_process])
            while q and q[0][1] == time:
                c, t = q.popleft()
                heapq.heappush(max_heap, c)

        return time

        heap =       n = 2
        queue [1, 3] [1, 4]
        time = 2