class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        while r < len(nums):
            while r < len(nums) and nums[r] == nums[r-1]:
                r += 1
            if r < len(nums):
                nums[l + 1] = nums[r]
                l += 1
            r = r + 1
        return l+1