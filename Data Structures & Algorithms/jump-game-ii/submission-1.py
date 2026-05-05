class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            min_jumps = float("inf")
            for j in range(nums[i]):
                if i + 1 + j < len(nums):
                    min_jumps = min(min_jumps, dp[i + 1 + j])
            dp[i] = 1 + min_jumps
        return dp[0]
                
    #     dp[i] = 1 + dp[min of 1...jump length]
    #     dp[i] = stores min number of jumps to reach the end
    #    ind 0 1 2 3 4 5
    #     dp 0 0 1 1 1 0    
    #        2 4 1 1 1 1    
    #          ? ? 