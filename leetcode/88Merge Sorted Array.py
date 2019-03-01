class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        # 对 nums2 里的每一个元素，在 nums1 里面进行二分查找，返回索引值，插在返回值的右侧

        for i in range(len(nums2)):
            index = self.binary_search(nums1, m+i, nums2[i])

            for j in range(m+i, index, -1):
                nums1[j] = nums1[j-1]

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




s = Solution()

nums1 = [4, 0, 0, 0, 0, 0]
nums2 = [1, 2, 3, 5, 6]
s.merge(nums1, 1, nums2, 5)




















