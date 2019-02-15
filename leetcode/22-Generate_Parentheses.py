class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left = n
        right = n
        res=[]
        self.DFS(n, n, res, "")
        print(res)
        return res


    def DFS(self, left, right, res, s_temp):
        if left == 0 and right == 0:
            res.append(s_temp)
            return
        if left > 0:

            self.DFS(left-1, right, res, s_temp+'(')
        if right > left:
            self.DFS(left, right-1, res, s_temp+")")


if __name__ == '__main__':
    obj = Solution()
    obj.generateParenthesis(3)