class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        from pprint import pformat

        if self.left is None and self.right is None:
            return str(self.val)
        return pformat({"%s" % (self.val): (self.left, self.right)}, indent=1)


"""
At the most 2 children each node
> Full : all nodes have 0 or 2 children nodes
> Complete: all levels except the last one has 2 children
> Perfect: all levels are full. 2^k -1 elements, where k is depth, starting with 1

** BST: Nodes values has to be ordered as left < parent < right
"""


class BinaryTree:
    def __init__(self):
        self.root = None

    #  left, parent, right.
    def in_order_traversal(self, root):
        if not root:
            return

        self.in_order_traversal(root.left)
        print(root.val, end="->")
        self.in_order_traversal(root.right)

    # left, right, parent
    def post_order_traversal(self, root):
        if not root:
            return

        self.in_order_traversal(root.left)
        self.in_order_traversal(root.right)
        print(root.val, end="->")

    # parent, left, right ==> Depth-First Search (DFS)
    def pre_order_traversal(self, root):
        if not root:
            return

        print(root.val, end="->")
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

    def bfs(self, root):
        if not root:
            return

    def get_max(self, node: TreeNode) -> TreeNode:
        if not node:
            return node

        if node.right:
            return self.get_max(node.right)
        return node

    def __remove(self, node, parent_node):
        if node.left and node.right:
            # remove max from left child
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

        if node.left and node.right:
            replacement_node = node.right
            node.right.left = node.left

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


    def add(self, val):
        if isinstance(val, list):
            for v in val:
                self.add(v)
            return

        new_node = TreeNode(val)

        if not self.root:
            self.root = new_node
            return

        node = self.root

        while True:
            if val == node.val:
                # duplicated
                break
            if val > node.val:
                if node.right is None:
                    node.right = new_node
                    break
                node = node.right
                continue
            # val < node.val
            if node.left is None:
                node.left = new_node
                break
            node = node.left


bt = BinaryTree()
bt.add([4,3,1,2])
print(bt.root)

print("\nIn Order:")
bt.in_order_traversal(bt.root)
print("\nPre Order:")
bt.pre_order_traversal(bt.root)
print("\nPost Order:")
bt.post_order_traversal(bt.root)

print("")
bt.remove(2)
print(bt.root)

bt = BinaryTree()
bt.add([4,2,6,1,3,5,7])
print(bt.pre_order_traversal(bt.root))
print(bt.root)
bt.remove(6)
print(bt.root)

# bt.invert()
