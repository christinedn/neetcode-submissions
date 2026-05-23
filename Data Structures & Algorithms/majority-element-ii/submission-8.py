class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        n = len(nums)
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[j-1]:
                j += 1
            if j - i > (n//3): 
                res.append(nums[i])
            i = j
        return res





