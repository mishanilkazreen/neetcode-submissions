class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(node):
            res = node

            while res != parents[res]:
                res = parents[res]
            return res
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
            
