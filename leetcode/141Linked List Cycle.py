# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        my_set = set()
        while head:
            if head not in my_set:
                my_set.add(head)
                head = head.next
            else:
                return False
        else:
            return True















