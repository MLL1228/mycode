
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        # length = len(strs)
        prefix = ''
        flag = True
        min_length = len(strs[0])

        for each_str in strs:
            min_length = min(min_length, len(each_str))
            print(min_length)

        for i in range(min_length):   # 以最短字符串为标准，逐个取出字符比较
            # print(strs[0][i])
            for j in strs:
                if j[i] != strs[0][i]:
                    flag = False
                    break
            if flag:
                prefix += strs[0][i]
                # print('prefix:  ', prefix)
            if not flag:
                break
        return prefix

s1 = Solution()
mylist = "134"
res = s1.longestCommonPrefix(mylist)
print(res)

