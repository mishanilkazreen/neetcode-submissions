# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return []
        self.res = 0

        def dfs(node, maxNum):
            if node.val >= maxNum:
                self.res += 1
            maxNum = max(maxNum, node.val)

            if node.left: dfs(node.left, maxNum)
            if node.right: dfs(node.right, maxNum)
        
        dfs(root, root.val)
        return self.res