class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        left = 0
        right = len(s) - 1
        
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
            
        
        string_alpha_num = "".join(c for c in s if c.isalnum())

        return string_alpha_num == string_alpha_num[::-1]
            
    
    
sol = Solution()
string1 = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(string1))