from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_mapper = {}
        for i, s in enumerate(strs):
            sorted_s = "".join(sorted(s))
            if not string_mapper.get(sorted_s):
                string_mapper[sorted_s] = []
            string_mapper[sorted_s].append(s)

        return list(string_mapper.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))