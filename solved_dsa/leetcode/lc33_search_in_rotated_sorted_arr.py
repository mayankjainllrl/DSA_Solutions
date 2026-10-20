

# cases:
"""_summary_

Returns:
    [6, 7, 1, 2, 3, 4, 5]
    [2, 4]
    [3, 1]
    [1]
"""
# if nums [left] < nums[right]
#       if mid > target:
#           right = mid - 1
#       else
#            left = mid + 1
# else:

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[left] < nums[right]:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            elif nums[mid] >= nums[left]:
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    if nums[left] > target:
                        left = mid + 1 
                    else:
                        right = mid - 1
            else:
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    if nums[right] >= target:
                        left = mid + 1 
                    else:
                        right = mid - 1
        
        return -1
    
sol = Solution()
nums = [5, 1, 3]
target = 3
print(sol.search(nums, target))