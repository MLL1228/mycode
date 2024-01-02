class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        len_nums = len(nums)
        for index, num in enumerate(nums):
            if num == 0:
                zero_count += 1
            else:
                if zero_count != 0:
                    nums[index - zero_count] = nums[index]

        for i in range(zero_count):
            nums[len_nums - i - 1] = 0
        print(nums)


Solution().moveZeroes([0, 1, 0, 3, 12])
