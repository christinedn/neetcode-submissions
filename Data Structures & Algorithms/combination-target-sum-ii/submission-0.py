class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # since there are duplicates
        res = []
        def dfs(start, currPath, currSum):
            if currSum == 0:
                res.append(currPath.copy())
                return
            if currSum < 0 or start >= len(candidates):
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue # cannot include duplicates at the same decision level
                currPath.append(candidates[i])
                dfs(i+1, currPath, currSum-candidates[i])
                currPath.pop()
                
        dfs(0, [], target)
        return res
