class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':

        if not needle:
            return 0

        for i in range(len(haystack)-len(needle)+1):
            len_needle = len(needle)

            if haystack[i] == needle[0]:
                # nonlocal flag
                flag = True
                for j in range(len_needle):

                    if haystack[i+j] != needle[j]:

                        flag = False
                        break

                if flag:
                    return i

        return -1


obj = Solution()
res = obj.strStr("hello", "ll")
print(res)