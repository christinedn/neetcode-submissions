class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adj_list = [[] for _ in range(n)]

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        def dfs(node):
            for nei in adj_list[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        for n in range(n):
            if n not in visited:
                visited.add(n)
                dfs(n)
                res += 1
        return res
