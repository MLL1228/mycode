def partion(nums, left, right):
    key = nums[left]
    while left < right:
        while left < right and nums[right] >= key:
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
        else:
            break
        while left < right and nums[left] < key:
            left += 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
        else:
            break
    return left



def quicksort(nums, left, right):
    if left < right:
        key_index = partion(nums, left, right)
        quicksort(nums, left, key_index)
        quicksort(nums, key_index+1, right)


nums = [5, 6, 3, 9, 10, 2, 7, 1, 4]
print (nums)
quicksort(nums, 0, len(nums)-1)
print (nums)