class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        p = len(a) - 1
        q = len(b) - 1
        carry = 0
        sum = ''
        while p >= 0 and q >= 0:
            if int(a[p]) + int(b[q]) + carry == 2:
                carry = 1
                sum = '0' + sum
            elif int(a[p]) + int(b[q]) + carry == 3:
                carry = 1
                sum = '1' + sum
            else:
                sum = str(int(a[p]) + int(b[q]) + carry) + sum
                carry = 0
            p -= 1
            q -= 1

        # print(sum, carry)
        if p < 0 and q < 0:
            if carry == 1:
                sum = '1' + sum
        elif p < 0 and q >= 0:
            for i in range(q, -1, -1):
                if int(b[i]) + carry == 2:
                    carry = 1
                    sum = '0' + sum
                elif int(b[i]) + carry == 3:
                    carry = 1
                    sum = '1' + sum
                else:
                    sum = str(int(b[i]) + carry) + sum
                    carry = 0
            if carry != 0:
                sum = '1' + sum
        elif p >= 0 and q < 0:
            for i in range(p, -1, -1):
                if int(a[i]) + carry == 2:
                    carry = 1
                    sum = '0' + sum
                elif int(a[i]) + carry == 3:
                    carry = 1
                    sum = '1' + sum
                else:
                    sum = str(int(a[i])+carry) + sum
                    carry = 0
            if carry != 0:
                sum = '1' + sum

        return sum

s = Solution()
res = s.addBinary("11", "1001")
print(res)













