# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 树的层序遍历，用到队列

class Node():
    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next

    # 这个函数是会在print的时候被自动调用，就是把这个Node显示出来
    def __repr__(self):
        return str(self.element)

class queue():

    # 初始化函数，自动被调用
    # 初始化Queue()类的时候，它有2个属性，分别指向头尾
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    # 如果 head 的 next 属性为空，则说明队列是空的
    def empty(self):
        return self.head.next is None

    # 入队操作
    def enqueue(self, element):
        n = Node(element)
        self.tail.next = n
        self.tail = n

    # 出队操作,head 不会动，始终是一个空节点。
    def dequeue(self):
        node = self.head.next
        if not self.empty():
            self.head.next = node.next
        return node

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """





    def








