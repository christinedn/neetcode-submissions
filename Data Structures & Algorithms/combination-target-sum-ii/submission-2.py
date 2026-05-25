class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(start, curr_path, curr_sum):
            if curr_sum == target:
                res.append(curr_path.copy())
                return
            for i in range(start, len(candidates)):
                # duplicates?
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if curr_sum + candidates[i] > target:
                    break
                curr_path.append(candidates[i])
                dfs(i+1,curr_path, curr_sum + candidates[i])
                curr_path.pop()
        dfs(0, [], 0)
        return res