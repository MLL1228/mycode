class Solution:
    def trap(self, height: list) -> int:
        """
        左右各一个指针
        calculated_height默认为0
        取较小的值short_height：
            如果short_height小于等于calculated_height，pass；
            如果short_height大于calculated_height，从左到右遍历：
                cur_sum默认为0
                如果该位置高度小于等于calculated_height，计算高度差short_height-calculated_height；
                如果该位置的高度大于calculated_height：
                    如果小于short_height，计算高度差short_height-height；
                    如果大于等于short_height，不做处理 ；
            calculated_height = max（calculated_height， short_height）
        小的一边移动指针
        """
        # total = 0
        # i = 0
        # j = len(height) - 1
        # calculated_height = 0
        # while i < j:
        #     short_height = min(height[i], height[j])
        #
        #     if short_height > calculated_height:
        #         k = i + 1
        #         cur_sum = 0
        #         while k < j:
        #             if height[k] <= calculated_height:
        #                 cur_sum += short_height - calculated_height
        #             else:
        #                 if height[k] < short_height:
        #                     cur_sum += short_height-height[k]
        #             k += 1
        #         total += cur_sum
        #         calculated_height = max(calculated_height, short_height)
        #
        #     if height[i] <= height[j]:
        #         i += 1
        #     else:
        #         j -= 1
        # return total
        """
        方法二
        建立两个列表：l_list存放此位置左边的最大值， r_list存放此位置右边的最大值
        设置l_max， r_max = 0
        for index in range(len(height))：
            l_max = max(height[index], l_max)
            r_max = max(height[len(height)-1-index], r_max)

            l_list.append(l_max)
            r_list.append(r_max)


        """
        l_list = list()
        r_list = list()
        l_max, r_max = 0, 0
        len_height = len(height)

        for index in range(len_height):
            l_max = max(height[index], l_max)
            r_max = max(height[len(height) - 1 - index], r_max)

            l_list.append(l_max)
            r_list.append(r_max)

        total = 0
        for index in range(len_height):
            short_height = min(l_list[index], r_list[len_height-1-index])
            if height[index] < short_height:
                total += short_height - height[index]
        return total


print(Solution().trap([4,2,0,3,2,5]))


