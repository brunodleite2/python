class Node:
    def __init__(self, value):
        self.value = value  # Assign data
        self.next = None  # Initialize next as null


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head:
            new_node.next = self.head
        self.head = new_node

    # Time complexity O(n)
    # Space complexity O(1) 
    def remove(self, value):
        node = self.head
       
        if not node:
            return

        if node.value == value:
            self.head = node.next
            return

        next_node = node.next

        while (next_node):
            if next_node.value == value:
                node.next = next_node.next
                return
            
            node = next_node
            next_node = next_node.next            

    def print(self):
        if (not self.head):
            print("Empty")
            return

        node = self.head

        while (node):
            print(node.value)
            node = node.next


# Code execution starts here
if __name__ == '__main__':
    llist = LinkedList()
    llist.remove(1)
    llist.print()

    llist.append(1)
    llist.print()

    llist.remove(1)

    llist.append(2)
    llist.append(2)
    llist.append(1)
    llist.append(1)
    llist.remove(1)
    llist.remove(2)
    llist.remove(2)
    llist.print()
