class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 1 or len(nums) == 2:
            return nums
        count_needed = len(nums)//3
        nums.sort()
        res = set()
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
                if count > count_needed:
                    res.add(nums[i])
            else:
                count = 1

        return list(res)


        [1]
        count_needed = 0
        count = 1

