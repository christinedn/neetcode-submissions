class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]: # left sorted
                if target < nums[l] or target > nums[m]: # search the other half
                    l = m + 1
                else: # search current half that we are in
                    r = m - 1
            else: # right sorted
                if target > nums[r] or target < nums[m]: # search the other half
                    r = m - 1
                else: # search the current half
                    l = m + 1
        return -1
