class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        q = deque()
        res = 0
        for i, n in enumerate(nums):
            if n != val:
                res += 1
            if n != val and q:
                index = q.popleft()
                nums[index] = n
                q.append(i)
            if n == val:
                q.append(i)
        return res
        