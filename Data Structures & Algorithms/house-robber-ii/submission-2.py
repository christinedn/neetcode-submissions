class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob1, rob2 = 0, 0
        for num in nums[:-1]:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        rob3, rob4 = 0, 0
        for num in nums[-1:0:-1]:
            temp = max(rob3 + num, rob4)
            rob3 = rob4
            rob4 = temp
        return max(rob2, rob4)