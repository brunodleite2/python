# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.root = None

    def get_max(self, node: TreeNode) -> TreeNode:
        if not node:
            return node

        if node.right:
            return self.get_max(node.right)
        return node


    def __remove(self, node, parent_node):
        if node.left and node.right:
            max_left_branch = self.get_max(node.left)
            self.remove(max_left_branch.val)
            node.val = max_left_branch.val
            return

        is_root = False
        if not parent_node:  # root
            is_root = True

        is_right_child = False
        if not is_root and node.val > parent_node.val:
            is_right_child = True

        replacement_node = None

        # only left child
        if node.left and not node.right:
            replacement_node = node.left

        # only left child
        if not node.left and node.right:
            replacement_node = node.right

        if is_root:
            self.root = replacement_node
            return

        if is_right_child:
            parent_node.right = replacement_node
            return
        parent_node.left = replacement_node


    def remove(self, val):
        node = self.root
        parent_node = None

        while node:
            if val > node.val:
                parent_node = node
                node = node.right
                continue

            if val < node.val:
                parent_node = node
                node = node.left
                continue

            # val == node.val:
            self.__remove(node, parent_node)
            break

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        self.root = root
        self.remove(key)

        return self.root