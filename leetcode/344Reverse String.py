class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """

        length = len(s)
        print(length)
        mid = (length-1) // 2
        print(mid)
        if not s:
            print('nothing')
            return s
        if length % 2 == 1:
            for i in range(mid):
                s[i], s[length-1-i] = s[length-1-i], s[i]
            print(s)
        else:
            for i in range(mid+1):
                s[i], s[length - 1 - i] = s[length - 1 - i], s[i]
            print(s)
            # return s

s = Solution()
# mys = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
mys = ['1', '2', '3', '4']
s.reverseString(mys)









