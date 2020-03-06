# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __remove(self, node, parent_node):


        is_right_child = False
        if node.val > parent_node.val:
            is_right_child = True

        replacement_node = None

        # leaf node
        if not node.left and not node.right:
            pass

        # only left child
        if node.left and not node.right:
            replacement_node = node.left

        # only left child
        if not node.left and node.right:
            replacement_node = node.right

        if node.left and node.right:
            replacement_node = node.right
            node.right.left = node.left

        if is_right_child:
            parent_node.right = replacement_node
            return
        parent_node.left = replacement_node

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        node = root
        val = key
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

            if not parent_node:  # root
                root = None
                break

            # val == node.val:
            self.__remove(node, parent_node)
            break



