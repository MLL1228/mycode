def bubblesort(arr):
    # flag = True
    # while flag:
    #     flag = False
    #     for i in range(len(arr)-1):
    #         if arr[i] > arr[i + 1]:
    #             arr[i], arr[i + 1] = arr[i + 1], arr[i]
    #             print('swap: %d, %d' % (i, i + 1))
    #             flag = True
    #     print(arr, flag)
    # return arr

    """
    遍历数组
    每一趟遍历比较两个相邻位置元素的大小，大的放右边，一趟下来最大的元素会被放到最右边
    :param arr:
    :return:
    """
    for i in range(len(arr)-1):
        flag = 1
        for e_index in range(len(arr)-i-1):
            if arr[e_index] > arr[e_index+1]:
                arr[e_index], arr[e_index+1] = arr[e_index+1], arr[e_index]
                flag = 0
        if flag == 1:
            break

    return arr


myarray = [8, 6, 0, 4, 2, 3, 9, 3, 1]

res = bubblesort(myarray)
print(res)