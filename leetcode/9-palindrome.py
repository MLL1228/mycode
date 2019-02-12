class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            mystr = str(x)
            reverse_str = mystr[::-1]
            # print(reverse_str)
            if int(reverse_str) == x:
                return True
            else:
                return False




if __name__ == '__main__':
    print(Solution().isPalindrome(-121))