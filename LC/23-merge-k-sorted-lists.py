<<<<<<< HEAD

=======
>>>>>>> 93306e2dad4e6dc7f8b061f3ec4ceddfeac9c0a1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

<<<<<<< HEAD
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        DONE = (2**31 -1) * -1
=======

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        DONE = (2**31 - 1) * -1
>>>>>>> 93306e2dad4e6dc7f8b061f3ec4ceddfeac9c0a1

        if not lists:
            return None

        pre_head = ListNode(-1)
        aux = pre_head

        def __get_min_and_move():
            vals = []

            for l in lists:
                vals.append(l.val)

            if not vals:
                return DONE

            minimum = min(vals)

            for index, l in enumerate(lists):
<<<<<<< HEAD
                if minimum == l.val: # move next when min is find on the list # first only
=======
                if minimum == l.val:  # move next when min is find on the list # first only
>>>>>>> 93306e2dad4e6dc7f8b061f3ec4ceddfeac9c0a1
                    lists[index] = l.next
                    break

            return minimum

        while True:
<<<<<<< HEAD
            lists = list(filter(None, lists)) # Filter None and Empty
=======
            lists = list(filter(None, lists))  # Filter None and Empty
>>>>>>> 93306e2dad4e6dc7f8b061f3ec4ceddfeac9c0a1

            minimum = __get_min_and_move()

            if minimum == DONE:
                break

            aux.next = ListNode(minimum)
            aux = aux.next
            continue

<<<<<<< HEAD

        return pre_head.next
=======
        return pre_head.next
>>>>>>> 93306e2dad4e6dc7f8b061f3ec4ceddfeac9c0a1
