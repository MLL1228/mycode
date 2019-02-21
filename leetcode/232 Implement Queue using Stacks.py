class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # s1 为负责 input 的栈
        # s2 为负责 output 的栈
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        # 在 s1 中直接加入元素x
        self.s1.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # s1： 1，2，3，4，5   需要把 1 从栈中弹出
        # 思路：依次弹出元素到 s2， 直到最后一个元素，然后再把这些元素装回 s1, s2 清空

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        ele = self.s2.pop()
        if not self.s1:
            while self.s2:
                self.s1.append(self.s2.pop())
        return ele




    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        ele = self.s2[-1]
        if not self.s1:
            while self.s2:
                self.s1.append(self.s2.pop())
        return ele


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.s1 == []
               #and self.s2 == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()