class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(currPath, start, target):
            if target == 0:
                res.append(currPath)
                return
            for i in range(start, len(nums)):
                if nums[i] > target:
                    break
                dfs(currPath + [nums[i]], i, target - nums[i])
            return
        dfs([], 0, target)
        return res


        

        
        
        
       


        