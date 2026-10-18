class Solution:
    def search(self, nums: list[int], target: int) -> int:
        upper = len(nums) - 1
        lower = 0   
        while lower <= upper:
            mid = (upper + lower) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lower = mid + 1
            else:
                upper = mid - 1   
        return -1
    
sol = Solution()
nums = [0, 1, 2]
target = 2
print(sol.search(nums, target))