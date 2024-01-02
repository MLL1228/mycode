class Solution:
    def longestConsecutive(self, nums: list) -> int:
        if len(nums) == 0:
            return 0

        sorted_nums = sorted(nums)
        longest_consecutive_length = 1
        cur_consecutive_length = 1

        index = 1
        while index < len(sorted_nums):
            if sorted_nums[index] - sorted_nums[index-1] == 1:
                cur_consecutive_length += 1
            elif sorted_nums[index] - sorted_nums[index-1] == 0:
                pass
            else:
                longest_consecutive_length = max(longest_consecutive_length, cur_consecutive_length)
                cur_consecutive_length = 1
            index += 1

        return max(longest_consecutive_length, cur_consecutive_length)


solution = Solution()
r = solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
print(r)






