class Solution:
    def groupAnagrams(self, strs: list) -> list:
        result = {}
        for estr in strs:
            estrs = "".join(sorted(estr))
            if "".join(sorted(estr)) in result:
                result[estrs].append(estr)
            else:
                result[estrs] = [estr]
        return list(result.values())


solution = Solution()
r = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(r)