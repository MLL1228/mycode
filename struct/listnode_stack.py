'''
栈的特点是后入先出
实现思想：
    初始化：创建一个空节点 ，是队列的属性 head
    入栈：每次创建一个新节点，插入到链表的开头，即让 head.next 指向它
    出栈：先判断栈不为空，让 head.next 指向head.next.next ，这样实现了出栈

有一个属性 head，始终指向栈链表的头部，是一个空节点
栈的操作主要有 判空、入栈 和 出栈
'''
class Node():
    def __init__(self, element=None, next = None):
        self.element = element
        self.next = next

    # 打印 s.pop 时，当 pop 出来的是一个节点，不是空的时候，打印节点会调用此方法
    # 当 pop 出来的是空的时候，就不会走到这里打印节点这一步，直接会print None
    def __repr__(self):
        return str(self.element)

class stack():
    def __init__(self):
        node = Node()
        self.head = node

    # 判断栈是否为空
    def empty(self):
        return self.head.next is None

    # 入栈操作..........创建一个 node，插入到链表开头。
    def push(self, element):
        node = Node(element, self.head.next)
        self.head.next = node

    def pop(self):
        node = self.head.next
        if not self.empty():
            self.head.next = node.next
        return node

# 测试函数
def test():
    s = stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())


if __name__ == '__main__':
    # 运行测试函数
    test()




