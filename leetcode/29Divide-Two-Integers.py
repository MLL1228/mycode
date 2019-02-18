class Solution:
    def divide(self, dividend: 'int', divisor: 'int') -> 'int':
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)

        res = 0
        while divisor <= dividend:
            #  初始化 除数
            div = divisor
            count = 1
            #  被除数大于当前除数 2 倍时，除数进行右移操作。 count 也要在本次循环基础上 * 2。
            while dividend >= div << 1:
                count <<= 1
                div <<= 1
            #   要记得在 被除数基础上减去 除数的值,  res 也要加上 count 的值
            res += count
            dividend -= div
            # print(divisor)
            if res >= 2147483647 and sign == 1:
                return 2147483647


        return res if sign==1 else -res


if __name__ == '__main__':
    s = Solution()
    r = s.divide(10, -3)
    print(r)