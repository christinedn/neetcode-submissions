class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set()

        # go through array, put numbers in set
        for n in nums:
            s.add(n)
        # find the one with no left neighbor, that is the starting sequence
        for n in nums:
            curRes = 1
            left_neighbor = n - 1
            if left_neighbor not in s:
                next_num = n + 1
                while next_num in s:
                    curRes += 1
                    next_num += 1
            # compare with res, take maximum
            res = max(res, curRes)
        return res

        