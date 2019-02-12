class Tree():
    def __init__(self, element=None):
        self.element = element
        self.left = None
        self.right = None

    # 树的遍历，是一个递归操作
    def pretravelsal(self):
        '''
        遍历数：根左右方法
        :return:
        '''
        print(self.element)
        if self.left is not None:
            self.left.travelsal()
        if self.right is not None:
            self.right.travelsal()

    def Nopreorder(self):

    # 树的每个节点，左右子树互换，递归方法。
    def reverse(self):
        self.left, self.right = self.right, self.left
        if self.left is not None:
            self.left.reverse()
        if self.right is not None:
            self.right.reverse()


# 手动创建二叉树
def test():
    t = Tree(0)
    t.left = Tree(1)
    t.left.left = Tree(2)
    t.left.right = Tree(3)
    t.right = Tree(4)
    t.right.left = Tree(5)
    t.right.right = Tree(6)

    # traversal
    t.pretravelsal()

    # reverse
    t.reverse()
    t.pretravelsal()


if __name__ == '__main__':
    test()















