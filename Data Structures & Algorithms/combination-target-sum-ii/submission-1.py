class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(start, curr_path, cur_sum):
            if cur_sum == target:
                res.append(curr_path.copy())
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue # discard duplicates at the same level
                if cur_sum + candidates[i] > target:
                    break
                curr_path.append(candidates[i])
                dfs(i+1,curr_path,cur_sum+candidates[i])
                curr_path.pop()

        dfs(0, [], 0)
        return res