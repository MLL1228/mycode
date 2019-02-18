class Solution:
    def countAndSay(self, n: 'int') -> 'str':
        res = self.say(n)
        return res







    def say(self, n):
        if n == 1:
            return '1'

        my_say = self.say(n-1)
        # print(my_say)


        count = 1
        pre = ''
        res = ''
        for i in my_say:
            if pre:
                if i == pre:
                    count += 1
                    pre = i

                else:
                    res += '%d%s' % (count, pre)
                    count = 1
                    pre = i

            else:
                pre = i


        res += '%d%s' % (count, pre)
        # print(res)

        return res

s = Solution()
s.countAndSay(5)














