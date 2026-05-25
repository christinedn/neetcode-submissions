class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while (l <= r):
            m = (l+r)//2
            # left sorted
            if nums[l] <= nums[m]:
                if target == nums[m]:
                    return m
                elif nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # right sorted
            else:
                if target == nums[m]:
                    return m
                elif nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
            