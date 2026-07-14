# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        cursum = 0
        temp = root
        result = []
        def traverse(node):
            if node.left is not None and node.val >= low:
                traverse(node.left)
            result.append(node.val)
            if node.right is not None and node.val <= high:
                traverse(node.right)
        traverse(root)
        for i in result:
            if i <= high and i >= low :
                cursum += i
        return cursum