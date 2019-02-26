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
    def threeSumClosest(self, nums, targets):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        diff = None

        if len(nums) < 3:
            return
        for i in range(len(nums)-1):
            target = targets - nums[i]
            for j in range(i+1, len(nums)):
                if j == i:
                    continue
                target1 = target - nums[j]
                for k in range(j+1, len(nums)):
                    if diff is None:
                        diff = abs(target1-nums[k])
                        result = [nums[i], nums[j], nums[k]]
                        tar_res = sum(result)
                    elif diff > abs(target1-nums[k]):
                        diff = abs(target1-nums[k])
                        result = [nums[i], nums[j], nums[k]]
                        tar_res = sum(result)

        return tar_res





















