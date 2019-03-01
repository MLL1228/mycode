class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.append(0)
        carry = 1
        flag = False
        # 最高位可能有进位
        for i in range(len(digits)-2, -1, -1):
            temp_sum = digits[i] + carry
            if temp_sum >= 10:
                carry = 1
                digits[i + 1] = temp_sum % 10
                if i == 0:
                    flag = True
                    digits[0] = carry
            else:
                carry = 0
                digits[i + 1] = temp_sum

        if not flag:
            return digits[1:]
        else:
            return digits

s = Solution()
res = s.plusOne([9])
print(res)










