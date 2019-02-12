def selectionsort(arr):
    for i in range(len(arr)-1):
        print('num: ', i)
        minnum = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minnum]:
                minnum = j
        arr[i], arr[minnum] = arr[minnum], arr[i]
        print(arr)
    return arr

myarray = [8, 6, 0, 4, 2, 3]

res = selectionsort(myarray)
print(res)