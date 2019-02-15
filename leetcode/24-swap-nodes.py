# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':

        if head:
            if head.next:
                myhead = head.next
                head.next = myhead.next
                myhead.next = head

                temp_head1 = head.next
                pre = head
                while temp_head1:
                    if temp_head1.next:
                        temp_head2 = temp_head1.next
                        temp_head1.next = temp_head2.next
                        temp_head2.next = temp_head1
                        pre.next = temp_head2

                        pre = temp_head1
                        temp_head1 = temp_head1.next

                    else:
                        break

                return myhead

            else:
                return head



        else:
            return head


hh = ListNode(1)
hh.next = ListNode(2)
hh.next.next = ListNode(3)
hh.next.next.next = ListNode(4)

obj = Solution()
res_head = obj.swapPairs(hh)
print(res_head.val)
while res_head.next is not None:
    res_head = res_head.next
    print(res_head.val)