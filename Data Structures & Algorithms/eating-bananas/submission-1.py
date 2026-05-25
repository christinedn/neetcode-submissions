import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            totalHours = 0

            for pile in piles:
                totalHours += math.ceil(pile / m)

            if totalHours > h:
                # too slow, need faster
                l = m + 1
            else:
                # fast enough, try slower
                res = m
                r = m - 1

        return res