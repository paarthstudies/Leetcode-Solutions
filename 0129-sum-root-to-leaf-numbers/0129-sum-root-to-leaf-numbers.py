# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        curr_list = []
        result = 0
        def traverse(node):
            nonlocal result
            curr_list.append(node.val)
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
            if node.left is None and node.right is None:
                temp = int("".join(map(str, curr_list)))
                result += temp
            curr_list.pop(-1)
        traverse(root)
        return result