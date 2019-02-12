class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        strip_str = str.strip()
        if strip_str == '':
            return 0
        # print(strip_str)
        res = ''

        # print(ord(strip_str[1]))
        if len(strip_str) >= 2:
            if strip_str[0] == '+' and ord(strip_str[1]) in range(48, 58):
                for i in strip_str[1:]:
                    if ord(i) in range(48, 58):
                        res = res + i
                    else:
                        break
                try:
                    res_int = int(res)
                except Exception as e:
                    return 2147483647
                else:
                    return res_int
            elif ord(strip_str[0]) in range(48, 58):
                for i in strip_str:
                    if ord(i) in range(48, 58):
                        res = res + i
                    else:
                        break
                # print(res)
                try:
                    res_int = int(res)
                except Exception as e:
                    return 2147483647
                else:
                    return res_int
            elif strip_str[0] == '-' and ord(strip_str[1]) in range(48, 58):
                # print('go')
                for i in strip_str[1:]:
                    if ord(i) in range(48, 58):
                        res = res + i
                        # print(res)
                    else:
                        break
                try:
                    res_int = -int(res)
                except Exception as e:
                    return -2147483648
                else:
                    if res_int < -2147483648:
                        return -2147483648
                    else:
                        return res_int
            else:
                return 0
        elif len(strip_str) == 1:
            if ord(strip_str[0]) in range(48, 58):
                return int(strip_str)
            else:
                return 0





mystr = '2147483648'
obj = Solution()
print(obj.myAtoi(mystr))
