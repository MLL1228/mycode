def bubblesort(arr):
    print("数组长度： %s" % len(arr))
    for i in range(len(arr)-1):  # 只剩最后一个元素的那一趟不用排序
        print("第%s次循环" % (i+1))
        print("循环范围：[0, %s]" % (len(arr)-i-2))
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print('swap: %d, %d' %(j, j+1))
        print(arr)
    return arr

myarray = [8, 6, 0, 4, 2, 3]

res = bubblesort(myarray)
print(res)