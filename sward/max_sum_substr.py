#  给出一个列表，有正数和负数，如 【1， 4， -5， 7， -1】
#  找出和最大的一串子数列
#  最大子数组和问题，使用动态规划 DP
import copy

def max_sum_substr(mylist):
    length = len(mylist)
    max_sum = 0
    temp_sum = 0
    res = []
    res_temp = []

    for i in range(length):
        temp_sum += mylist[i]
        res_temp.append(mylist[i])

        if temp_sum > max_sum:
            max_sum = temp_sum
            res = copy.deepcopy(res_temp)

        elif temp_sum < 0:
            temp_sum = 0
            res_temp=[]



    print(res)
    print(max_sum)

    return


te_list = [2, 4, -7, 5, 2, -1, 2, -4, 3]
max_sum_substr(te_list)








