class Solution:
    def removeElement(self, nums: 'List[int]', val: 'int') -> 'int':

        if not nums:
            return 0

        temp = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[temp] = nums[i]
                temp += 1

        print(nums)
        print(temp)
        return temp



obj = Solution()
obj.removeElement([2], 3)