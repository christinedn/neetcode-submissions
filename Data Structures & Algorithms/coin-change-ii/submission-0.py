class Solution:
    def change(self, target_amount: int, coins: List[int]) -> int:
        dp = [0] * (target_amount+1)
        dp[0] = 1
        for c in coins:
            for i in range(c, target_amount+1):
                dp[i] = dp[i] + dp[i-c]
        return dp[target_amount]

