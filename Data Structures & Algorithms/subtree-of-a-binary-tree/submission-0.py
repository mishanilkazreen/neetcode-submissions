# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if not subRoot: return True

        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.val == subRoot.val and self.compare(node, subRoot): return True
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return False

    def compare(self, a, b):
        if not a and not b: return True
        if not a or not b: return False
        return a.val == b.val and self.compare(a.left, b.left) and self.compare(a.right, b.right)

