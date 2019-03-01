class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1 = s.strip()
        if not s1:
            return 0
        sp_list = s1.split(' ')
        # if not sp_list:
        #     return len(s)
        # else:
        #     last_str = sp_list[-1]
        #     return len(last_str)
        for i in sp_list[-1::-1]:
            if i:
                last_str = i
                break
        return len(last_str)




so = Solution()
res = so.lengthOfLastWord(" ")
print(res)






