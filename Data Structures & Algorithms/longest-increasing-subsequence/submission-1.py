class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = 1 + dp[j]
        return max(dp)