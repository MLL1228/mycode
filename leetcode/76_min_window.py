class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = dict()
        for e_t in t:
            if e_t in dict_t:
                dict_t[e_t] += 1
            else:
                dict_t[e_t] = 1

        dict_s = dict()
        min_string = ""
        cur_string = ""
        s_index = 0
        while s_index < len(s):
            print(s_index)
            if cur_string:
                if s[s_index] in t:
                    if s[s_index] in dict_s:
                        if dict_s[s[s_index]] >= dict_t[s[s_index]] and cur_string.startswith(s[s_index]):
                            # 开始回退, 重置s_index
                            s_index = s_index + 1 - len(cur_string)
                            cur_string = ""
                            dict_s = dict()
                            continue
                        else:
                            cur_string = "".join([cur_string, s[s_index]])
                            dict_s[s[s_index]] = min(dict_s[s[s_index]]+1, dict_t[s[s_index]])
                    else:
                        cur_string = "".join([cur_string, s[s_index]])
                        dict_s[s[s_index]] = 1

                    if dict_s == dict_t:
                        if min_string:
                            if len(min_string) > len(cur_string):
                                min_string = cur_string
                        else:
                            min_string = cur_string
                        print("occur", cur_string)
                        # 开始回退, 重置s_index
                        s_index = s_index + 1 - len(cur_string) + 1
                        cur_string = ""
                        dict_s = dict()
                        continue
                else:
                    cur_string = "".join([cur_string, s[s_index]])
            else:
                if s[s_index] in t:
                    cur_string = "".join([cur_string, s[s_index]])
                    dict_s[s[s_index]] = 1
                    if dict_s == dict_t:
                        return s[s_index]
            s_index += 1
            print(cur_string)

        return min_string



print(Solution().minWindow("bba", "ab"))



