class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(i):
            if len(path) == k: # k = 2 (num elements)
                res.append(path.copy())
                return
            if i > n: # n = 3 (range)
                return
            path.append(i)
            dfs(i+1)
            path.pop()
            dfs(i+1)
        dfs(1)
        return res