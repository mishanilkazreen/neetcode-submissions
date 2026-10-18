class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(1, len(edges) + 1)}

        def connected(a, b):
            visit = set()
            stack = [a]
            visit.add(a)
            while stack:
                node = stack.pop()
                if node == b:
                    return True
                for nb in adj[node]:
                    if nb not in visit:
                        visit.add(nb)
                        stack.append(nb)
            return False

        for a, b in edges:
            if connected(a, b):
                return [a, b]
            adj[a].append(b)
            adj[b].append(a)

        return []