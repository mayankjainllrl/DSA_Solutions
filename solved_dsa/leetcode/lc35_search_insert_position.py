class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return 0 if right < 0 else ((left + right) // 2) + 1


sol = Solution()
nums = [1, 53]
target = 7

print(sol.searchInsert(nums, target))