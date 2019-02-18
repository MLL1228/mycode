class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> 'int':
        self.quicksort(nums, 0, len(nums)-1)
        res = self.binary_search(nums)
        # print(res)
        if res == -1:
            return 1
        else:
            temp = 1
            for i in range(res+1, len(nums)):
                if nums[i] - temp > 1:
                    return temp+1
                else:
                    temp = nums[i]
            else:
                return temp+1





    def partition(self, nums, l, r):
        key = nums[l]
        while l < r:
            while l < r and nums[r] >= key:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
            else:
                break
            while l < r and nums[l] < key:
                l += 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
            else:
                break
        return l


    def quicksort(self, nums, l, r):

        if l < r:
            key_index = self.partition(nums, l, r)
            self.quicksort(nums, l, key_index)
            self.quicksort(nums, key_index+1, r)
        return nums


    def binary_search(self, nums, target=1):
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
        return -1


# nums = [5, 6, 3, 9, 10, 2, 7, 1, 4]
s = Solution()
# s.quicksort(nums, 0, len(nums)-1)
# print(nums)

nums = [1,2,0]
res = s.firstMissingPositive(nums)
print(res)








