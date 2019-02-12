class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums.sort()
        res_set = set()

        for i in range(len(nums)):
            
