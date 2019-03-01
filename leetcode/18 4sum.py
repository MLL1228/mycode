class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res_list = []
        if len(nums) < 4:
            return res_list
        self.quicksort(nums, 0, len(nums)-1)
        print(nums)
        for i in range(len(nums)):
            if target > 0 and nums[i] > target:
                return res_list
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                tar1 = target - nums[i]
                for j in range(i+1, len(nums)):
                    if tar1 > 0 and nums[j] > tar1:
                        break
                    elif j > i+1 and nums[j] == nums[j-1]:
                        continue
                    else:
                        p = j+1
                        q = len(nums)-1
                        tar2 = tar1 - nums[j]

                        while p < q:
                            if nums[p] == nums[p-1] and p > j+1:
                                p += 1
                            elif q < (len(nums)-1) and nums[q] == nums[q+1]:
                                q -= 1
                            else:
                                if nums[p] + nums[q] == tar2:
                                    res_list.append([nums[i], nums[j], nums[p], nums[q]])
                                    p += 1
                                elif nums[p] + nums[q] > tar2:
                                    q -= 1
                                elif nums[p] + nums[q] < tar2:
                                    p += 1

        return res_list




    def partition(self, nums, left, right):
        key = nums[left]
        while left < right:
            while left < right and nums[right] >= key:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
            else:
                break
            while left < right and nums[left] < key:
                left += 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
            else:
                break
        return left

    def quicksort(self, nums, left, right):
        if left < right:
            index_key = self.partition(nums, left, right)
            self.quicksort(nums, left, index_key)
            self.quicksort(nums, index_key+1, right)



s = Solution()
nums = [1,-2,-5,-4,-3,3,3,5]
# s.quicksort(nums, 0, len(nums)-1)
# print(nums)
res = s.fourSum(nums, -11)
print(res)







