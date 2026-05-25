class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adj list
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # visit array (t/f) which represents if each node has been visited or not

        # call dfs on each neighbor in adj, this is responsibile for marking each as visited
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)

        # go through nodes in n, will check if it has arleady been visited (from dfs call)
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res
        
        