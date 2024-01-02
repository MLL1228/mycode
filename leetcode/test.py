class Solution:
    def two_sum(self, nums, target):
        for index1, num1 in enumerate(nums[:-1]):
            for index2, num2 in enumerate(nums[index1+1:]):
                if num1 + num2 == target:
                    return [index1, index2+index1+1]


if __name__ == '__main__':
        solution = Solution()
        result = solution.two_sum([3, 3], 6)
        print(result)



