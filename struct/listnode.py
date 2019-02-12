'''
列表主要实现的方法有 append prepend pop list_to_string
'''


class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

    # 在末尾添加一个元素
    def append(self, element):
        new_node = ListNode(element)
        while self.next is not None:
            self = self.next

        self.next = new_node

    # 在头部后面添加一个元素
    def prepend(self, element):
        new_node = ListNode(element)
        new_node.next = self.next
        self.next = new_node
        return new_node

    # 删除并返回末尾的元素的值
    def pop(self):
        p = self
        q = self
        while q.next is not None:
            p = q
            q = q.next
        p.next = None
        del q
        return p.val

    def list_to_string(self):
        s = ''
        s += str(self.val)
        while self.next is not None:
            self = self.next
            s += '%s%s' % ('->', str(self.val))
        return s


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

res = head.list_to_string()
print(res)
# while res.next is not None:
#     res = res.next
#     print(res.val)
while head.next is not None:
    head = head.next
    print(head.val)




