class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n == 1:
                return 1
            elif n == 2:
                return 2
            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]
        return dfs(n)