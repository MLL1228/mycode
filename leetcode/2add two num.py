# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # len1 = get_len(l1) - 1
        # len2 = get_len(l2) - 1

        def get_num(l):
            num = l.val
            count = 0
            while l.next != None:
                l = l.next
                count += 1
                num += l.val * (10 ** count)
            return num

        def get_ret(my_num):
            l_res_temp = ListNode(my_num % 10)
            l_res = l_res_temp
            my_num = my_num // 10
            while my_num > 0:
                l_res_temp.next = ListNode(my_num % 10)
                l_res_temp = l_res_temp.next
                my_num = my_num // 10
            return l_res

        num1 = get_num(l1)
        num2 = get_num(l2)
        num3 = num1 + num2

        return get_ret(num3)

    # def get_len(l):
    #     count = 1
    #     while l.next != None:
    #         count += 1
    #         l = l.next
    #     return count

