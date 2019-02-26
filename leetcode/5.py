class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        res = ''

        for i in range(length):
            ret = self.find_str(i-1, i+1, s, length)
            if ret is None:
                if len(res) < 1:
                    res = s[i]
            else:
                left, right = ret[0], ret[1]
                # print(left, right)
                if len(res) < right - left + 1:
                    res = s[left:right+1]

            ret = self.find_str(i, i + 1, s, length)
            if ret is None:
                if len(res) < 1:
                    res = s[i]
            else:
                left, right = ret[0], ret[1]
                # print(left, right)
                if len(res) < right - left + 1:
                    res = s[left:right + 1]


        return res



    def find_str(self, left, right, s, length):
        if left >=0 and right < length:
            if s[left] == s[right]:
                res = self.find_str(left-1, right+1, s, length)
                if res is None:
                    return left,right
                else:
                    return res
            else:
                return left+1, right-1
        else:
            return None







s = Solution()
res = s.longestPalindrome('abba')
print(res)






















