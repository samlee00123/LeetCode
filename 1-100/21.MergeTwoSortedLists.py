# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val < l2.val:
            l3 = ListNode(l1.val, None)
            l1 = l1.next
        else:
            l3 = ListNode(l2.val, None)
            l2 = l2.next

        node = l3
        while l1 or l2:
            if not l1:
                node.next = l2
                break

            if not l2:
                node.next = l1
                break

            if l1.val < l2.val:
                node.next = ListNode(l1.val, None)
                node = node.next
                l1 = l1.next
            else:
                node.next = ListNode(l2.val, None)
                node = node.next
                l2 = l2.next

        return l3
