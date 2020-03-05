class TreeNode:
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent
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

    """
    add(value) { /* ... */ }
    find(value) { /* ... */ }
    remove(value) { /* ... */ }
    getMax() { /* ... */ }
    getMin() { /* ... */ }
    dfs()
    bfs()
    """

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
        self.in_order_traversal(root.left)
        self.in_order_traversal(root.right)

    def bfs(self, root):
        if not root:
            return

    def __remove(self, node):
        if not node.parent:  # root
            self.root = None
            return

        is_right_child = False
        if node.val > node.parent.val:
            is_right_child = True

        # leaf node
        if not node.left and not node.right:
            if is_right_child:
                node.parent.right = None
                return
            node.parent.left = None
            return

        # only left child
        """ if node.left and not node.right:
            new_node = node.left

        if not node.left and node.right:
            new_node = node.right

        if is_right_child:
            node.parent.right = new_node
        else:
            node.parent.left = new_node
        new_node.parent = node.parent

        # only right child
        if not node.left and node.right:
            if is_right_child:
                node.parent.right = node.right
            else:
                node.parent.left = node.right

            node.right.parent = node.parent
            return

        # both children .. right is promoted as parent
        node.right.parent = node.parent


        if is_right_child:
            node.parent.right = node.right
 """


    def remove(self, val):
        node = self.root

        while node:
            if val > node.val:
                node = node.right
                continue

            if val < node.val:
                node = node.left
                continue

            # val == node.val:
            self.__remove(node)
            break

    def add(self, val):
        new_node = TreeNode(val, None)

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
                    new_node.parent = node
                    break
                node = node.right
                continue
            # val < node.val
            if node.left is None:
                node.left = new_node
                new_node.parent = node
                break
            node = node.left


bt = BinaryTree()
bt.add(4)
bt.add(3)
bt.add(1)
bt.add(2)

print("In Order:")
bt.in_order_traversal(bt.root)
print("")
print("Pre Order:")
bt.pre_order_traversal(bt.root)
print("")
print("Post Order:")
bt.post_order_traversal(bt.root)

bt.remove(2)
print("Post Order:")
bt.in_order_traversal(bt.root)
# bt.invert()
