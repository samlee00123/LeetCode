# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        parent = []
        parent.append(root)
        children = []

        traversal = []

        while parent:
            for i in parent:
                traversal.append(i.val)

                if i.right:
                    children.append(i.right)
                else:
                    traversal.append(0)

                if i.left:
                    children.append(i.left)

            parent = list(children)
            children.clear()

        return traversal

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.bfs(p) == self.bfs(q)
