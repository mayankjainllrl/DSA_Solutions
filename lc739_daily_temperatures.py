class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        cooler_days = []
        for i, temp in enumerate(temperatures):
            while cooler_days and temp > temperatures[cooler_days[-1]]:
                prev = cooler_days.pop()
                result[prev] = i - prev
            cooler_days.append(i)
                    
        return result
        
    
sol = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(temperatures)
print(sol.dailyTemperatures(temperatures))