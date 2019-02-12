def bubblesort(arr):
    print(len(arr))
    flag = True
    while flag:
        flag = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                print('swap: %d, %d' % (i, i + 1))
                flag = True
        print(arr, flag)
    return arr



        # for i in range(len(arr) - 1):  # 只剩最后一个元素的那一趟不用
        #     flag = False
        #     for j in range(len(arr) - i - 1):
        #         if arr[j] > arr[j + 1]:
        #             arr[j], arr[j + 1] = arr[j + 1], arr[j]
        #             print('swap: %d, %d' % (j, j + 1))
        #             flag = True
        #     print(i, arr)
    return arr

myarray = [8, 6, 0, 4, 2, 3, 9, 3, 1]

res = bubblesort(myarray)
print(res)