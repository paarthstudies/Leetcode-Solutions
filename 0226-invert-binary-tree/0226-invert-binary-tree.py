# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        def traverse(node):
            left = node.left
            right = node.right
            node.left = right
            node.right = left
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
        traverse(root)
        return root