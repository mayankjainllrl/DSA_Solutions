class Solution:
    def climbStairs(self, n: int) -> int:
        current_answer = 1
        prev_answer = 1
        prev_prev_answer = 1
        for _ in range(n-1):
            prev_prev_answer = prev_answer
            prev_answer = current_answer
            current_answer = prev_answer + prev_prev_answer
            
        return current_answer
    
sol = Solution()
print(sol.climbStairs(10))