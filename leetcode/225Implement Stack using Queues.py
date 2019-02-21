class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 用两个队列来实现一个栈  q1： 入栈操作  q2： 出栈操作
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q1.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        # 出栈操作： 先将 q1 里的元素依次到 q2中， 记录下最后一个出队列的元素（不放入 q2，做返回使用）。再将 q2 中的元素依次出队到 q1 中
        if not self.q2:
            while self.q1:
                temp_ele = self.q1.pop(0)
                print('pop', self.q1)
                if self.q1:
                    self.q2.append(temp_ele)
        if not self.q1:
            while self.q2:
                self.q1.append(self.q2.pop(0))
        return temp_ele

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if not self.q2:
            while self.q1:
                temp_ele = self.q1.pop(0)
                self.q2.append(temp_ele)
        if not self.q1:
            while self.q2:
                self.q1.append(self.q2.pop(0))
        return temp_ele

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q1 == []

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.pop()
param_4 = obj.empty()