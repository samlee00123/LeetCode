# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        parent = []
        parent.append(root)
        depth = 0
        NotFound = True

        while NotFound:
            children = []
            for i in range(len(parent)):
                if parent[i] is None:
                    continue
                else:
                    if parent[i].left is None and parent[i].right is None:
                        NotFound = False
                        break
                    else:
                        children.append(parent[i].left)
                        children.append(parent[i].right)
            parent = list(children)
            depth += 1
        return depth
