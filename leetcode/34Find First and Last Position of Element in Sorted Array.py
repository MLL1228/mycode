class Solution:
    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        res = []
        flag = True
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
                break
        else:
            res = [-1, -1]
            flag = False


        if flag:
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] == target:
                    res.append(i)
                    break

        return res


s = Solution()
mynum = [5, 7, 7, 8, 8, 10]
tar = 8
myres = s.searchRange(mynum, tar)
print(myres)








