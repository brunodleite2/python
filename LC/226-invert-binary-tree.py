# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        if not root.left and not root.right:
            return root

        # Swap
        # root.left, root.right = root.right, root.left
        temp = root.left
        root.left = root.right
        root.right = temp



        self.invertTree(root.left)
        self.invertTree(root.right)

        return root