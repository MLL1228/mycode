class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)

        # 总个数为奇数，寻找位置为 len/2 的数字
        if (len1+len2)%2 == 1:
            index = len/2
            if len1/2 == len2/2:















