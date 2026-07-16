# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = []
        results = []
        queue.append(root)
        while len(queue) > 0:
            level_size = len(queue)
            current = []
            
            for i in range(level_size):
                node = queue[0]
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                current.append(node.val)
                queue.pop(0)
                
            results.append(current)
        return results