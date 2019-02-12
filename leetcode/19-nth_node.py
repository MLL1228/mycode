# Definition for singly-linked list.
import listnode

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        q = head
        count = 1
        flag = False
        flag_head = False

        # print('head.val:', head.val)
        while q.next is not None:
            if count > n:
                p = p.next
                flag_head = True
                # print('p: ', p.val)
            q = q.next
            # print('q: ', q.val)
            count += 1
            flag = True

        print('q: ', q.val)
        print('p: ', p.val)
        if not flag:
            return

        if flag_head or count > n:
            temp = p.next
            print('temp : ', temp.val)
            if temp.next != None:
                p.next = temp.next
                del temp
                # print('del: ', temp.val)

            else:
                p.next = None
                del temp


        else:
            head = head.next

        return head







head = listnode.ListNode(1)
head.next = listnode.ListNode(2)
# head.next.next = listnode.ListNode(3)
# head.next.next.next = listnode.ListNode(4)

s1 = Solution()
res = s1.removeNthFromEnd(head, 1)
if res != None:
    print(res.val)
    # print('111')
    # print(head.next is None)
    while res.next is not None:
        res = res.next
        print(res.val)


