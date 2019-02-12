class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        letter_dict = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }

        trans_list = []

        for i in digits:
            trans_list.append(letter_dict[int(i)])
            # print('trans list:', trans_list)

        res_list = self.get_combination(trans_list)
        return res_list



    def get_combination(self, list_of_str):
        if len(list_of_str) == 1:
            append_list = []
            for i in list_of_str[0]:
                append_list.append(i)
            return append_list

        length = len(list_of_str)
        print(length)


        while length > 1:
            # print('>>>>>>>>>>2')
            print(list_of_str)
            append_list = []

            str1 = list_of_str[0]
            str2 = list_of_str[1]
            for i in str1:
                for j in str2:
                    append_element = '%s%s' % (i, j)
                    append_list.append(append_element)
            # print('append_list', append_list)
            del list_of_str[0]
            del list_of_str[0]
            list_of_str.insert(0, append_list)
            length -= 1

        return list_of_str[0]

test_str = "234"
s1 = Solution()
res = s1.letterCombinations(test_str)
print(res)




