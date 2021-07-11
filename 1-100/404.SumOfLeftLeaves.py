# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        s = 0

        if not root:
            return s

        if root.left and not root.left.left and not root.left.right:
            s = root.left.val

        if root.left:
            s += self.sumOfLeftLeaves(root.left)

        if root.right:
            s += self.sumOfLeftLeaves(root.right)

        return s
