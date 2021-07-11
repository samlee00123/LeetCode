# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        traversal = {}
        parent = []
        children = []
        m = 1

        parent.append(root)

        while parent:
            for i in parent:
                if not i.val in traversal:
                    traversal[i.val] = 1
                else:
                    traversal[i.val] += 1
                    if traversal[i.val] >= m:
                        m = traversal[i.val]

                if i.right:
                    children.append(i.right)
                if i.left:
                    children.append(i.left)

            parent = list(children)
            children.clear()

        return [key for key, value in traversal.items() if value == m]
