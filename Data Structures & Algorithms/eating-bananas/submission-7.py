class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = maxEatingSpeed = max(piles)
        # perform binary search on 1 .... maxEatingSpeed
        l, r = 1, maxEatingSpeed
        while l <= r:
            m = (l+r)//2
            currHour = 0
            for n in piles:
                currHour += math.ceil(n/m)
            if currHour <= h: # we can eat at a slower rate
                res = m
                r = m - 1
            else: # currHour > h, we have to eat at a faster rate
                l = m + 1
        return res



        