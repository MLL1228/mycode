import math
import copy
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return s
        res = s[0]
        length = len(s)

        for i in range(length):
            temp_s = s[i]
            res = self.find_str(temp_s, s, i, i+1, length, res)
        return res

    def find_str(self, temp_s, s, start, next, length, res):
        if next >= length:
            return res
        len_temp = len(temp_s)
        # 超过数组的一半，就不应该再继续向下找
        if len_temp > math.ceil((length-start)/2):
            return res
        else:
            # 进入回文字符串判断
            if next < length and temp_s[-1] == s[next]:
                res = self.is_palind(temp_s, s, next, length, res, 0)

            # 将下一个字符加入 temps ， 进入更深一层地调用。
            temp_s += s[next]

            # abcba 形势判断   cur: abc
            if next+1 < length and temp_s[-2] == s[next+1]:
                res = self.is_palind(temp_s, s, next+1, length, res, 1)


            if next+1 < length:
                res = self.find_str(temp_s, s, start, next + 1, length, res)

        return res

    # is_palind
    def is_palind(self, temp_s, s, next, length, res, mytype):
        if mytype == 0:
            for i in temp_s[-1::-1]:
                if next >= length or i != s[next]:
                    return res
                next += 1
            else:
                if len(res) < (len(temp_s) * 2):
                    # print(len(res), res, len(temp_s), temp_s, len(res) < len(temp_s) * 2)
                    res = copy.deepcopy(temp_s) + copy.deepcopy(temp_s[-1::-1])
                    # print(res)
                else:
                    return res
        elif mytype == 1:
            for i in temp_s[-2::-1]:
                if next >= length or i != s[next]:
                    return res
                next += 1
            else:
                if len(res) < len(temp_s) * 2-1:
                    res = copy.deepcopy(temp_s) + copy.deepcopy(temp_s[-2::-1])
                    # print(res)
                else:
                    return res
        return res


s = Solution()
res = s.longestPalindrome('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(res)






















