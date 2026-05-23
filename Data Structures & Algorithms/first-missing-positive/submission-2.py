class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            while nums[i] - 1 != i and 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]: 
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
        for i, n in enumerate(nums):
            if n-1 != i:
                return i + 1
        return len(nums)+1


        # 0 1 2
        # 1 2 4

        # index: 0 1 2  3  4 5 6
        # value: 1 2 4* 5* 6 3 1

        # index: 0 1 2  3  4 5 6
        # value: 1 2 5* 4  6* 3 1

        # index: 0 1 2  3  4  5 6
        # value: 1 2 3* 4  5* 6 1

        # index: 0 1 2  3  4   5 6
        # value: 1 2 5* 4  6*  3 1

        # index: 0 1 2  3  4   5  6
        # value: 1 2 6* 4  5   3* 1

        # index: 0 1 2  3  4  5  6
        # value: 1 2 3  4   5  6  1


        # index: 0 1 2 3 4 5 6
        # value: 1 2 5 4 3 6 1

        