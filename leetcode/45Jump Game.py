# 思路是选择能跳到的范围内数值最大的数

class Solution:
    def jump(self, nums: 'List[int]') -> 'int':
        cur = 0
        count = 0
        for index in range(len(nums)):
            while cur + nums[cur] < len(nums) - 1:
                max_val = max(i for i in nums[cur + 1, cur + nums[cur]])
                cur =    














