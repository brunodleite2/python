# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        DONE = (2**31 - 1) * -1

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
                if minimum == l.val:  # move next when min is find on the list # first only
                    lists[index] = l.next
                    break

            return minimum

        while True:
            lists = list(filter(None, lists))  # Filter None and Empty

            minimum = __get_min_and_move()

            if minimum == DONE:
                break

            aux.next = ListNode(minimum)
            aux = aux.next
            continue

        return pre_head.next
