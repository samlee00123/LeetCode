# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        traversal = []
        parent = []
        children = []

        parent.append(root)

        while parent:
            level = []

            for i in parent:
                level.insert(0, i.val)
                if i.right:
                    children.append(i.right)
                if i.left:
                    children.append(i.left)

            parent = list(children)
            children.clear()
            traversal.insert(0, level)

        return traversal
