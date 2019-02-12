def bubblesort(arr):
    print(len(arr))
    for i in range(len(arr)-1):  # 只剩最后一个元素的那一趟不用排序
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print('swap: %d, %d' %(j, j+1))
        print(i, arr)
    return arr

myarray = [8, 6, 0, 4, 2, 3]

res = bubblesort(myarray)
print(res)