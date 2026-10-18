class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        x = x
        while left <= x:
            mid = (left + x) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                x = mid - 1
        return left - 1
    
sol = Solution()
print(sol.mySqrt(8))