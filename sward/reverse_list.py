class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse_list(mylist :'List[int]') -> 'list':
    cur = mylist
    pre_node = None
    while cur is not None:
        temp = cur
        cur = temp.next
        temp.next = pre_node
        pre_node = temp

    while temp is not None:
        print(temp.val)
        temp = temp.next


    return temp


head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)

reverse_list(head)










