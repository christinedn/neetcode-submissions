class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)
        
        for num in range(len(nums)+1):
            if num not in s:
                return num
            
