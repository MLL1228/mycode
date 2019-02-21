class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        # 进行二分查找，插在返回值的右侧

        for i in range(len(nums2)):
            index = self.binary_search(nums1, m+i, nums2[i])
            # if index == -1:
            #     for i in range(len(nums2)):
            #         nums1[i] = nums2[i]
            #     break
            # print(index)

            for j in range(m+i, index, -1):
                nums1[j] = nums1[j-1]
            # if index == 0 and nums1[0] > nums2[i]:
            #     nums1[index] = nums2[i]
            # else:
            nums1[index+1] = nums2[i]
            print(nums1)




    def binary_search(self, nums, m, target):
        for i in range(m):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i - 1
        else:
            return m-1
        # left = 0
        # mid = 0
        # right = m-1
        # print(left, right)
        # if left > right:
        #     return -1
        #
        # while left < right:
        #     mid = (left + right)//2
        #     print(mid)
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         right = mid-1
        #     elif nums[mid] < target:
        #         left = mid+1
        # else:
        #     return mid



s = Solution()

nums1 = [4, 0, 0, 0, 0, 0]
nums2 = [1, 2, 3, 5, 6]
s.merge(nums1, 1, nums2, 5)




















