# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre_head = ListNode(-1)
        aux = pre_head

        while True:
            if not l1 and not l2:
                break

            if not l1:
                aux.next = ListNode(l2.val)
                l2 = l2.next
                aux = aux.next
                continue

            if not l2:
                aux.next = ListNode(l1.val)
                l1 = l1.next
                aux = aux.next
                continue

            if l1.val < l2.val:
                aux.next = ListNode(l1.val)
                l1 = l1.next
            else:
                aux.next = ListNode(l2.val)
                l2 = l2.next
            aux = aux.next

        return pre_head.next