# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        right = self.maxDepth(root.right)
        left = self.maxDepth(root.left)

        return max(right+1, left+1)

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        if not root.left and not root.right:
            return True

        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
