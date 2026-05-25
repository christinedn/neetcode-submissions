class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        curr_postfix = 1
        for i in range(len(nums)):
            if i == 0:
                continue
            if i > 0:
                res[i] = nums[i-1] * res[i-1]

        for i in range(len(nums)-1, -1, -1):
            curr_prefix = res[i]
            res[i] = curr_prefix * curr_postfix
            curr_postfix = nums[i] * curr_postfix
        
        return res
        

