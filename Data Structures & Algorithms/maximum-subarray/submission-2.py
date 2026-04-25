class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            if currentSum < 0:
                currentSum = nums[i]
            else:
                currentSum += nums[i]
            maxSum = max(maxSum, currentSum)
        return maxSum

        