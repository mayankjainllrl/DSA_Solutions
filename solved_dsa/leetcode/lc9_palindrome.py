# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False

#         num = x
#         palindrome_num = []
#         while x > 0:
#             palindrome_num.append(str(x%10))
#             x = x // 10
            
#         return int("".join(palindrome_num)) == num
            
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num = x
        other_num = 0
        while x > 0:
            other_num = other_num * 10 + x%10
            x = x // 10
            
        return other_num == num

sol = Solution()
print(sol.isPalindrome(1214121))