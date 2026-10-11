# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        bfs = deque([(root, 0)])
        res = defaultdict(list)

        while bfs:
            node, depth = bfs.popleft()
            res[depth].append(node.val)
            if node.left: bfs.append((node.left, depth + 1))
            if node.right: bfs.append((node.right, depth + 1)) 
        return list(res.values())