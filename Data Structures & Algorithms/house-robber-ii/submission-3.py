def helper(arr):
    prev2, prev1 = 0, 0
    for n in arr:
        new = max(prev2 + n, prev1)
        # increment pointers
        prev2 = prev1
        prev1 = new
    return prev1

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[:-1]), helper(nums[1:]))
        