class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        left = 0
        right = x

        if x < 1:
            return 0
        while left<=right:
            temp = (left + right)//2
            if temp*temp < x:
                res = temp
                left = temp+1
            elif temp*temp == x:
                return temp
            elif temp*temp > x:
                right=temp-1
        return res

s = Solution()
res = s.mySqrt(1)
print(res)











