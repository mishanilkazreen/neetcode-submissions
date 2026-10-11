# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        bfs = deque([root])
        res = []

        while bfs:
            level = []
            for _ in range(len(bfs)):
                node = bfs.popleft()
                level.append(node.val)
                if node.left: bfs.append(node.left)
                if node.right: bfs.append(node.right)
            res.append(level)
        return res