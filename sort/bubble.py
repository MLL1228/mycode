def bubbleSort(arr):
    for i in range(1, len(arr)):
        print('num:   ', i)
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)
        print('finish: ', arr)
    return arr

myarray = [1, 6, 0, 4, 2]

res = bubbleSort(myarray)
print(res)