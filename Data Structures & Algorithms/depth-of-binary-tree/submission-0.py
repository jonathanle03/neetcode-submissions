# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfsDepth(root, 0)

    def dfsDepth(self, root: Optional[TreeNode], depth: int) -> int:
        if root:
            depth += 1
            depth = max(self.dfsDepth(root.left, depth), self.dfsDepth(root.right, depth))
        return depth