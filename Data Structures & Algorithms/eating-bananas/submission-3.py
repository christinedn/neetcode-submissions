class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxEatingSpeed = max(piles)
        l = 1
        r = maxEatingSpeed
        res = float('inf')
        while l <= r:
            currEatingSpeed = (l+r)//2
            currEatingHours = 0
            for i in range(len(piles)):
                currEatingHours += math.ceil(piles[i]/currEatingSpeed)
            if currEatingHours > h:
                l = currEatingSpeed + 1
            elif currEatingHours <= h:
                r = currEatingSpeed - 1
                res = currEatingSpeed
        return res
