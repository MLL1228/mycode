class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums[-1])
            nums.pop(-1)
        print(nums)


s = Solution()
s.rotate([1, 2, 3, 4, 5, 6, 7], 3)