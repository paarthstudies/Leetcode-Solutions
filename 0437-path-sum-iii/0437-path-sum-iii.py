# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        
        count = 0
        currsum = 0

        hashmap = {}
        hashmap[0] = 1

        def traverse(root):
            nonlocal currsum, count 
            currsum += root.val
            diff = currsum - targetSum
            
            if diff in hashmap:
                count += hashmap.get(diff, 0)
            hashmap[currsum] = hashmap.get(currsum, 0) + 1
            
            if root.left is not None:
                traverse(root.left)
            if root.right is not None:
                traverse(root.right)

            hashmap[currsum] -= 1
            currsum -= root.val
        traverse(root)
        return count

