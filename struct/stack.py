# Node类是一个节点，有两个属性，一个存储元素，一个存储指向另一个节点的引用
class Node():
    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next

    # 这个函数是会在print的时候被自动调用，就是把这个Node显示出来
    def __repr__(self):
        print('1111111')
        return str(self.element)


class Mystack():
    # 初始化函数，自动被调用
    # 初始化Stack()类的时候，它有一个head属性，值是一个空的Node
    def __init__(self):
        self.head = Node()

    # 如果head的next属性为空，则说明栈是空的
    def is_empty(self):
        return self.head.next is None

    # 创建一个node，并让它指向当前head.next指向的元素，再把head.next指向它
    def push(self, element):
        self.head.next = Node(element, self.head.next)

    # 取出head.next指向的元素，如果栈不是空的，就让head.next指向node.next，这样node就不在栈中了
    def pop(self):
        node = self.head.next
        if not self.is_empty():
            self.head.next = node.next
        return node

    # head.next就是栈里面第一个元素
    def top(self):
        return self.head.next

# 测试函数
def test():
    s = Mystack()

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