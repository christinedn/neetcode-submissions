class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        min_length = float("inf")
        curr_sum = 0
        while r < len(nums):
            curr_sum += nums[r]
            while curr_sum >= target:
                min_length = min(r-l+1, min_length)
                curr_sum -= nums[l]
                l += 1
            r += 1
        
        # r has reached the end at this point.
        # but what if we could form a smaller subarray with l? we have to keep incrementing to check
        # while l < len(nums) and curr_sum >= target:
        #     min_length = min(r-l+1, min_length)
        #     curr_sum -= nums[l]
        #     l += 1

        return 0 if min_length == float("inf") else min_length
        # [2,1,5,1,5,3]
        #        l      r
