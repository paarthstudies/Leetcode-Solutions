class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False

        def findout(node, subnode):
            if node is None and subnode is None:
                return True
            if node is None or subnode is None:
                return False
            if node.val != subnode.val:
                return False

            return findout(node.left, subnode.left) and findout(node.right, subnode.right)

        if findout(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)