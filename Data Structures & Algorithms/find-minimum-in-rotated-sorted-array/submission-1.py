class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float("inf")
        while l <= r:
            # sorted
            if nums[l] < nums[r]:
                return nums[l]
            m = (l+r)//2
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m
        return res

        