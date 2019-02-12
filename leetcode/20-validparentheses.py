class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = ''
        match = {']': '[', '}': '{', ')': '('}
        input = ['(', '[', '{']

        while s:
            # try:
            #     flag = True
            #     match[s[0]]
            # except Exception:
            #     flag = False

            if not stack or s[0] in input or stack[-1] != match[s[0]]:
                print('1111')
                stack += s[0]
                s = s[1:]
            else:
                stack = stack[0:-1]
                s = s[1:]
        if not stack:
            return True
        else:
            return False

strs = ''
s1 = Solution()
res = s1.isValid(strs)
print(res)


