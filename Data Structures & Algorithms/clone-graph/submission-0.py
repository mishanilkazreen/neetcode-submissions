"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        oldToNew = {node: Node(node.val)}
        queue = deque([node])
        while queue:
            nod = queue.popleft()
            for nb in nod.neighbors:
                if nb not in oldToNew:
                    oldToNew[nb] = Node(nb.val)
                    queue.append(nb)

        for old, new in oldToNew.items():
            for nb in old.neighbors:
                new.neighbors.append(oldToNew[nb])

        return oldToNew[node]