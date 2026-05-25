class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(c):
            d = 1
            curr_weight = 0
            for w in weights:
                if curr_weight + w > c:
                    d += 1
                    curr_weight = 0
                    if d > days:
                        return False
                curr_weight += w
            return True
        left = max(weights)
        right = sum(weights)
        res = sum(weights)
        while left <= right:
            m = (left+right)//2
            if (can_ship(m)):
                res = m
                right = m - 1
            else:
                left = m + 1
        return res


        # wrong
        # d = 0
        # curr_weight = 0
        # for w in weights:
        #     curr_weight += w
        #     if curr_weight > c:
        #         d += 1
        #         curr_weight = 0
        #         if d > days:
        #             return False
        # if curr_weight > c:
        #     return False
        # return True