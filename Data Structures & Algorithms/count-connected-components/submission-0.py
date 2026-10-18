class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # create adj list
        adjList = {i:[] for i in range(n)}
        for parent, child in edges:
            adjList[parent].append(child)
            adjList[child].append(parent)

        visit = set()
        components = 0

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for adj in adjList[node]:
                dfs(adj)

        for node in range(n):
            if node in visit:
                continue
            
            dfs(node)
            
            components += 1
        
        return components