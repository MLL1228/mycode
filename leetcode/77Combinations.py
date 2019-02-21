import copy
# class Solution(object):
#     def combine(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         # 思路， 先取前 k-1 个数字， 遍历从 range(k, n+1), 两部分依次组合
#         #         取前 k-2 个数字 + 第 k 个数字， 遍历从 range（k+1， n+1），两部分依次组合
#         #         .......
#         #         这一次循环内循环 k-1 次
#         # 最外部循环，循环 n - k + 1 次, 每次循环第一个元素都是 i+1
#         res_list = []
#
#         if k == 1:
#             # temp_list = []
#             for ind in range(n):
#                 res_list.append([ind+1])
#                 # res_list.append(copy.deepcopy(temp_list))
#             return res_list
#
#         for i in range(n-k+1):  # [0, n-k]
#             mylist = []
#             for item in range(k):  # [0 , k-1]
#                 mylist.append(item + i + 1)  # 一个完整的列表， [i ， k+i]
#                 for j in range(k, 1, -1):
#                     mylist.remove(j + i)
#                     for item_next in range(k + i, n + 1):
#                         if item_next not in mylist:
#                             mylist.append(item_next)
#                             res_list.append(copy.deepcopy(mylist))
#                             mylist.remove(item_next)
#                     mylist.append(j + i)
#
#
#         return res_list

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """


        for i in range(n):
            temp_list = []
            temp_list.append(i+1)





    def find_next_ele(self, temp_list, n, k):
        length = len(temp_list)
        max_num = max(temp_list)
        if length < k:
            for i in range(max_num, n+1):
                temp_list.append(max_num+1)












s = Solution()
print(s.combine(4, 3))





