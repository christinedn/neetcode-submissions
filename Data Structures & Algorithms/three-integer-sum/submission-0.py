class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i, n in enumerate(nums[:-2]):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if (nums[i] + nums[j] + nums[k]) > 0:
                    k -= 1
                elif (nums[i] + nums[j] + nums[k]) < 0:
                    j += 1
                else:
                    res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    j += 1
                    k -= 1
        return [list(t) for t in res]