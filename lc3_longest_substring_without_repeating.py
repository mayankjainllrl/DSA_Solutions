class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window = 0
        seen = {}
        for i, c in enumerate(s):
            if c in seen and seen[c] >= window:
                longest = max(longest, i - window)
                window = seen[c] + 1
            seen[c] = i

        return max(longest, len(s) - window)   
    
    
    
sol = Solution()
s = "rttewrwpoiuytrer"
print(sol.lengthOfLongestSubstring(s))