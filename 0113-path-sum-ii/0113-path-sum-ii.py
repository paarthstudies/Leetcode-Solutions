# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        result = []
        curr_list = []
        def traverse(node, remaining, curr_list):
            curr_list.append(node.val)
            remaining -= node.val
            if (node.left is None and node.right is None) and remaining == 0:
                result.append(list(curr_list))
                
            if node.left is not None:
                traverse(node.left, remaining, curr_list)
            if node.right is not None:
                traverse(node.right, remaining, curr_list)
            curr_list.pop(-1)
            return result
        return traverse(root, targetSum, curr_list)