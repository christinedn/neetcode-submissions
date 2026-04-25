class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, currPath, target):
            if target == 0:
                res.append(currPath)
                return
            if target < 0 or i >= len(nums):
                return
            dfs(i, currPath + [nums[i]], target - nums[i])
            dfs(i+1, currPath, target)
        dfs(0, [], target)
        return res


        