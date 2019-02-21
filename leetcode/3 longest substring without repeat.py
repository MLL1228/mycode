# 思路： res: 纪录结果，初始化为空    longst_s： 遍历时纪录当前最长子字符串
#   对 s 每一个字符进行遍历：   longst_s 初始化只有此字符，继续对接下来的字符进行遍历
#       如果该字符没有出现在 longst_s 中，longst_s就加入此字符，直到出现已存在的字符把循环 break。 比较 longst_s 和 res 长度， res 选取 长度较长的字符串。
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # longest_s = ''
        res = ''
        len_of_s = len(s)

        # print(len_of_s)

        for i in range(len_of_s):
            longest_s = s[i]
            for j in range(i + 1, len_of_s):
                if s[j] not in longest_s:
                    longest_s += s[j]
                else:
                    break
            # print(len(longest_s))
            # print(len(res))
            if len(longest_s) > len(res):
                res = longest_s

        return len(res)
