# import copy
# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res_list = []
#         length = len(nums)
#         k = 3
#         target = 0
#
#         for i in range(len(nums)):
#             if i > length - k:
#                 break
#             temp_list = []
#             temp_list.append(nums[i])
#             self.find_res(temp_list, i+1, 1, 3, res_list, nums, length, target-nums[i])
#             temp_list.pop()
#
#         return res_list
#
#     def find_res(self, temp_list, next, now_k, k, res_list, nums, length, target):
#         if length-next < k - now_k:
#             return
#         if now_k >= k:
#             return
#         if k-now_k == 2:
#             count = 0
#             for item in nums[next::]:
#                 temp_list.append(item)
#                 tar = target - item
#                 count += 1
#                 # print(temp_list, item, nums[next+1::])
#                 for fin in nums[next+count::]:
#                     if fin == tar:
#                         temp_list.append(tar)
#                         fin_list = copy.deepcopy(temp_list)
#                         fin_list.sort()
#                         if fin_list not in res_list:
#                             res_list.append(copy.deepcopy(fin_list))
#                         temp_list.pop()
#                 temp_list.pop()
#
#
#         for i in nums[next:]:
#             temp_list.append(i)
#             self.find_res(temp_list, next+1, now_k+1, k, res_list, nums, length, target-i)
#             temp_list.pop()

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.quicksort(nums, 0, len(nums)-1)
        # result_list = []
        if len(nums) < 3:
            return result_list
        for i in range(len(nums)-1):
            if nums[i] > 0:
                return result_list
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                target = 0 - nums[i]
                # print(nums[i], target)
                # 设置两个指针 p ，q，分别指向 i+1， len（nums）-1， 寻找两数相加和为 target 的下标，直到 p >= q
                p = i+1
                q = len(nums)-1
                lastp = nums[p] - 1
                lastq = nums[q] + 1

                while p < q:
                    if nums[p] != lastp and nums[q] != lastq:
                        if nums[p] + nums[q] > target:
                            lastq = nums[q]
                            q -= 1
                        elif nums[p] + nums[q] < target:
                            lastp = nums[p]
                            p += 1
                        else:
                            return [nums[i], nums[p], nums[q]]
                            result_list.append([nums[i], nums[p], nums[q]])
                            lastp = nums[p]
                            lastq = nums[q]
                            p += 1
                    elif nums[p] == lastp:
                        p += 1
                    elif nums[q] == lastq:
                        q -= 1

        return result_list

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
nums = [-1, 0, 1, 2, -1, -4]
# s.quicksort(nums, 0, len(nums)-1)
# print(nums)
res = s.threeSum(nums)
print(res)


















