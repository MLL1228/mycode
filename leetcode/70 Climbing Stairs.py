class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        #
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        nums = [0, 1, 2]
        if n < 3:
            return nums[n]
        for i in range(3, n+1):
            nums.append(nums[i-1] + nums[i-2])

        return nums[n]



s = Solution()
print(s.climbStairs(36))


