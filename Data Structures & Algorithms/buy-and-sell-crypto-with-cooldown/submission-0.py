class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # key (i, buy (boolean) - tells us if we can buy on this day), val = max_profit
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            if buy: # we dont have a dont have a stock and we can buy
                buying = dfs(i+1, not buy) - prices[i]
                cooldown = dfs(i+1, buy)
                dp[(i, buy)] = max(buying, cooldown)
            else:
                sellling = dfs(i+2, not buy) + prices[i]
                cooldown = dfs(i+1, buy)
                dp[(i, buy)] = max(sellling, cooldown)
            return dp[(i, buy)]
        return dfs(0, True)
        
        