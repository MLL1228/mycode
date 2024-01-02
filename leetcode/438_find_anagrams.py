class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        """
        1. list_anagrams = list()
        2. 遍历p，p的所有不同字符作为字典p_dic的key，value为出现的次数
        3. 遍历s, cur_string = s[index: index+len(p)]
        4. 遍历 p_dic，看每一个key在cur_string中出现的次数是否相等

        :param s:
        :param p:
        :return:
        """
        list_anagrams = list()
        p_dict = dict()
        for c in p:
            if c in p_dict:
                p_dict[c] += 1
            else:
                p_dict[c] = 1

        for index in range(0, len(s)-len(p)+1):
            cur_string = s[index: index + len(p)]
            for uc in p_dict:
                if cur_string.count(uc) != p_dict[uc]:
                    break
            else:
                list_anagrams.append(index)

        return list_anagrams


print(Solution().findAnagrams("ababababab", "aab"))





