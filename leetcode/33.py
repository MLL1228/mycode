class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        if not nums:
            return -1

        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:  # 说明目前 两个指针 还是在两个递增序列中，需要向右缩小范围进行查找
                l = mid+1
            else:  # 说明目前 两个指针 是在右边的同一个递增序列中了，需要向左缩小范围进行查找边界值
                r = mid

        # print(nums[mid])


        if nums[l-1] == target and l != 0:
            return l-1
        # if l == 0 and nums[l] == target:
        #     return 0
        #
        # if nums[0] > target:
        res1 = self.binary_search(nums, l, len(nums)-1, target)
        if res1 != -1:
            return res1
        # else:
        res2 = self.binary_search(nums, 0, l-1, target)
        if res2 != -1:
            return res2

        return -1



    def binary_search(self, nums, left, right, target):

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                return mid
        return -1


mynum = [1,3]
tar = 3
s = Solution()
res = s.search(mynum, tar)
print(res)