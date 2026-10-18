class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nb in adj[node]:
                dfs(nb)

        dfs(0)
        return len(visit) == n