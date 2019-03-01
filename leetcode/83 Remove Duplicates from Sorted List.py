# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        cur = head
        pre = cur
        while cur is not None:
            cur = cur.next
            if cur is not None:
                if cur.val == pre.val:
                    pre.next = cur.next
                else:
                    pre = cur
        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(4)

s = Solution()
res = s.deleteDuplicates(head)

# while res.next is not None:
#     res = res.next
#     print(res.val)
while res is not None:
    print(res.val)
    res = res.next







