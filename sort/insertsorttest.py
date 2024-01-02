def insertsort(nums):
    length = len(nums)
    for i in range(1, length):
        key = nums[i]
        for j in range(i, -1, -1):
            if nums[j-1] > key:
                nums[j] = nums[j-1]
            else:
                break
        nums[j] = key

arr = [4, 3, 7 ,8 ,4 , 4 ,5]
insertsort(arr)
print(arr)