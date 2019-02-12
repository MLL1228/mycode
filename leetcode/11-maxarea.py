# class Solution:
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         max_area = 0
#         for i in range(len(height)):
#             for j in range(len(height)):
#                 hei = min(height[i], height[j])
#                 width = j - i
#                 area = hei * width
#                 if max_area < area:
#                     max_area = area
#         return max_area

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        i = 0
        j = length - 1
        max_area = (j-i)*min(height[j], height[i])

        while i != j:
            if height[i] >= height[j]:
                j -= 1
                area = (j-i)*min(height[j], height[i])
                max_area = max(max_area, area)

            else:
                i += 1
                area = (j - i) * min(height[j], height[i])
                max_area = max(max_area, area)
        return max_area





if __name__ == '__main__':
    arr = [1,8,6,2,5,4,8,3,7]
    obj = Solution()
    res = obj.maxArea(arr)
    print(res)