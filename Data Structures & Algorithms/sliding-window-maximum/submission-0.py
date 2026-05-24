class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # populate deque, maintaining monotonic structure
        l, r = 0, 0
        q = deque()
        res = []
        while r < len(nums):
            while q and nums[r] >= nums[q[-1]]:
                q.pop()
            q.append(r)
            if r-l+1 == k:
                res.append(nums[q[0]])
                if l == q[0]:
                    q.popleft()
                l += 1
            r += 1
        return res



# index = 0 1 2 3 4 5 6 7 8 10
# values= 2 7 3 1 6 2 5 8 1 4
#         ^     ^
# deque = size of k
# 7 2 1     
# 1 2 3