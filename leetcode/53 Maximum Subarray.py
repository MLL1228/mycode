# 思路： 如果前面的加起来 < 0 ，那么前面的都舍弃掉
#       如果加到某个地方 数值开始变小， 那么就先记录下最大值，直到小于0时，这一串丢弃掉
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        max_num = max(nums)
        cur_num = 0
        for i in nums:
            if cur_num + i < 0:
                cur_num = 0
            elif cur_num + i >= 0:
                if cur_num + i > max_num:
                    max_num = cur_num + i
                cur_num = cur_num + i
        return max_num


s = Solution()
nums = [1, -1, 1]
res = s.maxSubArray(nums)
print(res)

