class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_p = 0
        lowest_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > lowest_price:
                price_diff = prices[i] - lowest_price
                if price_diff > max_p:
                    max_p = price_diff
            else:
                lowest_price = prices[i]
        return max_p
    
    
sol = Solution()
prices = [10, 7, 5, 11, 33, 2, 1, 30]
print(sol.maxProfit(prices))