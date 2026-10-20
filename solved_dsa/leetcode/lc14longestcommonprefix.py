class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        smallest_str = min(strs, key=lambda x: len(x))
        common_prefix = smallest_str
        for str_i in strs:
            if len(common_prefix) <= 0:
                break
            while not str_i.startswith(common_prefix) and len(common_prefix) > 0:
                common_prefix = common_prefix[:-1]
        
        return common_prefix
    
    
sol = Solution()
strings = ["flower","flo","flight", "f"]
print(sol.longestCommonPrefix(strings))