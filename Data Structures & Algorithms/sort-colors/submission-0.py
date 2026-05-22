class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3
        for n in nums:
            count[n] += 1
        
        curr_index = 0
        for i, c in enumerate(count):
            while c != 0:
                nums[curr_index] = i
                curr_index += 1
                c -= 1
        return nums