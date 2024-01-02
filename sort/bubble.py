def bubble_sort(arr):
    for i in range(1, len(arr)):
        print('第 %s 次循环' % i)
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)
        print('finish: ', arr)
    return arr


myarray = [1, 2, 6, 0, 4, 2, 3]

res = bubble_sort(myarray)
print(res)


