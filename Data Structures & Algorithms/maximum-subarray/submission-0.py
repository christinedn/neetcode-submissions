class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, runningSum = nums[0], nums[0]
        for n in nums[1:]:
            runningSum = max(runningSum + n, n)
            res = max(runningSum, res)
        return res