def selectionsort(arr):
    # for i in range(len(arr)-1):
    #     print('第%s轮' % i)
    #     min_index = i
    #     for j in range(i+1, len(arr)):
    #         if arr[j] < arr[min_index]:
    #             min_index = j
    #     arr[i], arr[min_index] = arr[min_index], arr[i]
    #     print("交换后：%s" % arr)
    # return arr

    """
    遍历数组，每一轮选出最小的元素同当前位置交换
    :param arr:
    :return:
    """
    for i in range(len(arr)-1):
        min_index = i
        for e_index in range(i+1, len(arr)):
            if arr[e_index] < arr[min_index]:
                min_index = e_index
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


myarray = [8, 6, 0, 4, 2, 3]
res = selectionsort(myarray)
print("最终：%s" % res)