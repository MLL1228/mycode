class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':

        if not nums:
            return 0

        length = len(nums)

        temp = 0
        for i in range(1, length):
            if nums[temp] != nums[i]:
                temp += 1
                nums[temp] = nums[i]

        print(nums)
        print(temp+1)
        return temp+1




obj = Solution()
obj.removeDuplicates([])
