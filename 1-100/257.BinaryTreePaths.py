# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: TreeNode, path: str, paths: List[str]) -> List[str]:
        if not node.left and not node.right:
            path += str(node.val)
            paths.append(path)
            return paths

        if node:
            path += str(node.val) + "->"

        if node.right:
            self.dfs(node.right, path, paths)

        if node.left:
            self.dfs(node.left, path, paths)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        paths = []
        self.dfs(root, "", paths)
        return paths
