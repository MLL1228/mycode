# def insert_sort(arr):
#     length = len(arr)
#     for i in range(1, length):
#         print("i为 %s" % i)
#         for j in range(i, 0, -1):
#             # j为当前位置，试探j-1位置
#             # 如果当前数较小，插入到前面
#             if arr[j] < arr[j-1]:
#                 print("前移交换 %s 给 %s" % (arr[j - 1], arr[j]))
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#                 print(arr)
#             else:
#                 # 没有进行交换，说明现在的位置是对的
#                 break
#
#
# def print_arr(arr):
#     for item in arr:
#         print(item)
#
#
# arr = [4, 3, 7, 8, 4, 4, 5]
# insert_sort(arr)
# print(arr)


def insertsort(arr):  #参数的传入，当想传入的是一个list时，直接传入一个变量就行了
    """
    从index 1 位置开始，该位置元素同前一元素比较。 比前一元素大的话进行交换
    再从index 2 位置开始比较， 2和1比较，1和0比较。 2和1比较时如果没有交换位置，则可以直接break，因为2比1大且上一轮排序保证了1一定比0大，所以2所在的位置是正确的
    ...
    :param arr:
    :return:
    """
    for i in range(len(arr)-1):
        for e_index in range(i+1, 0, -1):
            if arr[e_index] < arr[e_index-1]:
                arr[e_index], arr[e_index-1] = arr[e_index-1], arr[e_index]
            else:
                break
    return arr


l=[1,3,2,8,5,3,1]
print(insertsort(l))

