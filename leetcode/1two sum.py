class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        flag = False
        count = 0
        for i in nums[:-1]:
            num = target - i
            for j in nums[count:]:
                if j == num:
                    result.append(count)
                    result.append(nums.index[j])
                    flag = True
                    break
            if flag:
                break
            count += 1
        return result


