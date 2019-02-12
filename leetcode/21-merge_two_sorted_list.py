# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val >= l2.val:
            # print('l1.val >= l2.val')
            head = ListNode(l2.val)
            p = head
        else:
            head = ListNode(l1.val)
            p = head

        while True:
            if l1.val < l2.val:
                # print(l1.val)
                # print(l2.val)
                q = l1
                # q.next = None
                p.next = q
                p = p.next
                if l1.next is None:
                    l1 = None
                    break
                else:
                    l1 = l1.next

            else:
                # print(l1.val)
                # print(l2.val)
                # print('l2.next.val:  ', l2.next.val)
                q = l2
                # print('l2.next.val:  ', l2.next.val)
                # q.next = None
                p.next = q
                # print('l2.next.val:  ', l2.next.val)
                p = p.next
                # print('l2.next.val:  ', l2.next.val)

                if l2.next is None:
                    l2 = None
                    break
                else:
                    l2 = l2.next
                    # print(l2.val)

        if l1 is None:
            p.next = l2
        else:
            p.next = l1
            print(p.next.val)

        return head.next


h1 = ListNode(1)
p = h1
h1.next = ListNode(2)
h1.next.next = ListNode(4)

# del h1.next
# print(p)
#
# p.next = None
# print(h1.next)



# while p.next is not None:
#     p = p.next
#     print(p.val)


h2 = ListNode(1)
h2.next = ListNode(3)
h2.next.next = ListNode(4)

s1 = Solution()
res = s1.mergeTwoLists(h1, h2)
while res.next is not None:
    print(res.val)
    res = res.next
print(res.val)



