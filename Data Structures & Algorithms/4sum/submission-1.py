class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = len(nums)-1
                new_target = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == new_target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif nums[l] + nums[r] < new_target:
                        l += 1
                    else:
                        r -= 1
        return res

        # nums=[3,2,3,-3,1,0]     target=3           3 - (-3) - 0 = 6
        # [-3,0,1,2,3,3]
        #   i j   l   r
        # [-3,0,3,3]