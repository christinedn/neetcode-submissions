class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1 # most significant bit (1, 2, 4, 8)
        for i in range(1, n+1):
            if i == offset * 2: # if the number hits 2, 4, 8 change offset
                offset *= 2
            dp[i] = 1 + dp[i - offset]
        return dp
        
