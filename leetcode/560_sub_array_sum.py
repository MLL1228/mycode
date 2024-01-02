class Solution:
    def subarraySum(self, nums: list, k: int) -> int:

        # 超出时间限制
        """

        count = 0

        for index, i in enumerate(nums):
            print(index, i)
            if i == k:
                count += 1
            sum = k - i

            for j in nums[index+1:]:
                print("    j: "+str(j))
                if j == sum:
                    count += 1
                    print("    count: " + str(count))
                sum = sum - j

        return count
        """

        count = 0
        sum = 0
        sums_dict = {0: 1}
        for i in nums:
            sum += i
            if sum-k in sums_dict:
                count += sums_dict[sum-k]
            if sum in sums_dict:
                sums_dict[sum] = sums_dict[sum] + 1
            else:
                sums_dict[sum] = 1
        return count


solution = Solution()
print(solution.subarraySum([0, 0, 0], 0))





