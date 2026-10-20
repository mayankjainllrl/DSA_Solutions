

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        i = 0
        j = len(numbers) - 1
        while i < j:
            if target == numbers[i] + numbers [j]:
                return [i + 1, j + 1]
            elif target > numbers[i] + numbers [j]:
                i += 1
            else:
                j -= 1

    
    
sol = Solution()
numbers = [3,2,11,3]
target = 6
print(sol.twoSum(numbers, target))