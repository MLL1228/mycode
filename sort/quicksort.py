# def quickSort(arr, left=None, right=None):
#     left = 0 if not isinstance(left, (int, float)) else left
#     right = len(arr)-1 if not isinstance(right,(int, float)) else right
#     if left < right:
#         partitionIndex = partition(arr, left, right)
#         quickSort(arr, left, partitionIndex-1)
#         quickSort(arr, partitionIndex+1, right)
#     return arr
#
#
# def partition(arr, left, right):
#     pivot = left
#     index = pivot+1
#     i = index
#     while  i <= right:
#         if arr[i] < arr[pivot]:
#             swap(arr, i, index)
#             index+=1
#         i+=1
#     swap(arr,pivot,index-1)
#     return index-1
#
#
# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]
#
#
# my_array = [1, 6, 4, 2, 9, 2, 5, 1, 7]
# res = quickSort(my_array)
# print(res)
#


def quick_sort(arr, left, right):
    """
    1. 以arr[0]的值为基准，记为left，arr[-1]记为right
    2. right：比基准小arr[left] = arr[right],left++，同时 arr[right]空出来，再看left和基准比较 ； 比基准大就 right--
    3. left：比基准小就 left ++ ； 比基准大就 arr[right] = arr[left], right -- , 同时left位置空出来，再看right和基准比较
    4. 这样left==right结束排序后，基准在的位置一定是正确的。再把基准左右两侧的数组用同样的方法排序
    :param arr:
    :return:
    """
    if left >= right:
        return

    init_left, init_right = left, right
    pivot = arr[left]
    while left < right:
        # 先从右指针开始比较
        while arr[right] >= pivot and left < right:
            right -= 1
        if left < right:
            arr[left] = arr[right]
            left += 1
        # 再从左指针比较，比较完成后继续循环从右指针比较
        while arr[left] < pivot and left < right:
            left += 1
        if left < right:
            arr[right] = arr[left]
            right -= 1
    arr[left] = pivot

    quick_sort(arr, init_left, left-1)
    quick_sort(arr, left+1, init_right)

    return arr


my_array = [1, 6, 4, 2, 9, 2, 5, 1, 7]

res = quick_sort(my_array, 0, len(my_array)-1)
print(res)




