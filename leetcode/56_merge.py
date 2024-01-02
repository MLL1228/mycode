class Solution:
    def merge(self, intervals: list) -> list:
        intervals = sorted(intervals, key=lambda x: x[0])

        merge_list = list()
        for i in intervals:
            if merge_list:
                if merge_list[-1][1] >= i[0]:
                    merge_list[-1][1] = max(i[1], merge_list[-1][1])
                else:
                    merge_list.append(i)
            else:
                merge_list.append(i)
        return merge_list



s = Solution()
nums = [[1,3],[2,6],[8,10],[15,18]]
res = s.merge(nums)
print(res)