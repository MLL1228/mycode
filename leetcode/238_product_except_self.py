class Solution:
    def productExceptSelf(self, nums: list) -> list:

        # 时间复杂度：O(N) 空间复杂度： O(N)
        l_list, r_list = list(), list()

        # l_list 表示当前位置左侧元素的乘积，第一个元素左侧没有元素值设置为1
        for i in range(len(nums)):
            if i == 0:
                l_list.append(1)
            else:
                l_list.append(l_list[-1] * nums[i-1])

        # r_list 表示当前位置右侧元素的乘积
        for i in reversed(range(len(nums))):
            if i == len(nums)-1:
                r_list.append(1)
            else:
                r_list.append(r_list[-1] * nums[i+1])
        r_list = list(reversed(r_list))

        answer = list()

        for i in range(len(nums)):
            answer.append(l_list[i] * r_list[i])

        return answer


s = Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))