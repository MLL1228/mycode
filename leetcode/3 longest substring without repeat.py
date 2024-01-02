# 思路： res: 纪录结果，初始化为空    longst_s： 遍历时纪录当前最长子字符串
#   对 s 每一个字符进行遍历：   longst_s 初始化只有此字符，继续对接下来的字符进行遍历
#       如果该字符没有出现在 longst_s 中，longst_s就加入此字符，直到出现已存在的字符把循环 break。 比较 longst_s 和 res 长度， res 选取 长度较长的字符串。
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         # longest_s = ''
#         res = ''
#         len_of_s = len(s)
#
#         # print(len_of_s)
#
#         for i in range(len_of_s):
#             longest_s = s[i]
#             for j in range(i + 1, len_of_s):
#                 if s[j] not in longest_s:
#                     longest_s += s[j]
#                 else:
#                     break
#             # print(len(longest_s))
#             # print(len(res))
#             if len(longest_s) > len(res):
#                 res = longest_s
#
#         return len(res)

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        1. cur_string="" , longest_string=0 从初始位置开始遍历
        2. 如果当前字符不在cur_string，加入进去
        3. 如果当前字符在 cur_string, longest_string=max(len(cur_string), longest_string) 且 将已有字符及其之前的都移走，新的加入赋值给cur_string
        """
        cur_string = ""
        longest_string = 0
        for c in s:
            if c not in cur_string:
                cur_string = "".join([cur_string, c])
            else:
                longest_string = max(longest_string, len(cur_string))
                cur_string.index(c)
                cur_string = "".join([cur_string.split(c)[1], c])
        longest_string = max(longest_string, len(cur_string))

        return longest_string


print(Solution().lengthOfLongestSubstring("pwwkew"))