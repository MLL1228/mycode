class Solution:
    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':

        l = 0
        r = len(nums) -1

        while l <= r:
            index = l
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
                index = l
        else:
            if index > len(nums)-1:
                index = len(nums) -1
            if nums[index] > target:
                return index
            else:
                return index+1

s = Solution()
res = s.searchInsert([1, 3, 5, 6], 0)
print(res)



