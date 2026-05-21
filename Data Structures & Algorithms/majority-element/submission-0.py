class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        majority = nums[0]
        for n in nums:
            if n == majority:
                votes += 1
            else:
                votes -= 1
                if votes == 0:
                    # set new majority
                    votes = 1
                    majority = n 
        return majority