class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:

        # 超出时间限制
        # if k == 1:
        #     return nums
        #
        # max_num_list = list()
        # for index, enum in enumerate(nums[0:-k+1]):
        #     max_num = nums[index]
        #     for j in nums[index:index+k]:
        #         if max_num < j:
        #             max_num = j
        #     max_num_list.append(max_num)
        #
        # return max_num_list

        # 建立堆（优先队列)
        """
        import heapq
        max_num_list = list()
        nums_heap = list()
        for i in range(k):
            heapq.heappush(nums_heap, (-nums[i], i))
            # print(nums_heap)

        max_num_list.append(-nums_heap[0][0])
        # print("max_num_list: %s" % max_num_list)
        for j in range(k, len(nums)):
            heapq.heappush(nums_heap, (-nums[j], j))
            # print(nums_heap)
            while nums_heap[0][1] <= j-k:
                heapq.heappop(nums_heap)
                # print("heappop: %s" % nums_heap)
            max_num_list.append(-nums_heap[0][0])
            # print("max_num_list: %s" % max_num_list)

        return max_num_list
        """

        # 单调队列（双端队列deque实现）
        from collections import deque
        index_deque = deque()
        max_num_list = list()
        for i in range(k):
            while index_deque and nums[index_deque[-1]] < nums[i]:
                index_deque.pop()
            index_deque.append(i)
            # print(index_deque)
        max_num_list.append(nums[index_deque[0]])

        for j in range(k, len(nums)):
            while index_deque:
                if index_deque[0] <= j-k:
                    index_deque.popleft()
                elif nums[index_deque[-1]] < nums[j]:
                    index_deque.pop()
                else:
                    break
            index_deque.append(j)
            # print("index_deque: %s" % index_deque)
            max_num_list.append(nums[index_deque[0]])

        return max_num_list


solution = Solution()
print(solution.maxSlidingWindow([1,3,1,2,0,5], 3))