class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict1 = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        res = ''

        thousand = num // 1000
        res += dict1[1000] * thousand

        hundred = (num % 1000) // 100
        if hundred == 9:
            res += dict1[100] + dict1[1000]
        elif hundred < 9 and hundred >= 5:
            res += dict1[500] + dict1[100] * (hundred - 5)
        elif hundred == 4:
            res += dict1[100] + dict1[500]
        else:
            res += dict1[100] * hundred

        ten = (num % 100) // 10
        if ten == 9:
            res += dict1[10] + dict1[100]
        elif ten < 9 and ten >= 5:
            res += dict1[50] + dict1[10] * (ten - 5)
        elif ten == 4:
            res += dict1[10] + dict1[50]
        else:
            res += dict1[10] * ten

        single = (num % 10)
        if single == 9:
            res += dict1[1] + dict1[10]
        elif single < 9 and single >= 5:
            res += dict1[5] + dict1[1] * (single - 5)
        elif single == 4:
            res += dict1[1] + dict1[5]
        else:
            res += dict1[1] * single


        return res