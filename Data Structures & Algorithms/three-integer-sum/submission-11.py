class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-2, 0, 0, 2, 2]
        res = []
        nums.sort()
        # target, left, right
        # left + right = [ ] 4
        for target in range(0, len(nums)-2, 1):
            if target > 0 and nums[target] == nums[target-1]:
                continue
            left = target + 1
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] + nums[target] == 0:
                    res.append([nums[left], nums[right], nums[target]])
                    left = left + 1
                    while left < right and nums[left] == nums[left-1]:
                        left = left + 1
                    right = right - 1
                    while left < right and nums[right] == nums[right+1]:
                        right = right - 1
                    print("curr target:", target)
                elif nums[left] + nums[right] + nums[target] > 0:
                    right = right - 1
                else:
                    left = left + 1
        return res



