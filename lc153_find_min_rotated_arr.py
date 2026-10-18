"""Two Pointer Approach My Version"""
# class Solution:
#     def findMin(self, nums: list[int]) -> int:
#         start = 0
#         end = len(nums) - 1
#         while start <= end:
#             if nums[start] <= nums[end]:
#                 if end == len(nums) - 1:
#                     return nums[start]
#                 return nums[end+1]
#             elif nums[start] >= nums[start+1]:
#                 return nums[start+1]
#             end -= 1
#             start += 1
#         return nums[len(nums)-1]

"""Optimal Approach My Version"""
# class Solution:
#     def findMin(self, nums: list[int]) -> int:
#         start = 0
#         end = len(nums) - 1
#         while start <= end:
#             mid = (start + end) // 2
#             if mid + 1 >= len(nums):
#                 return nums[mid]
#             elif nums[mid] > nums[mid + 1]:
#                 return nums[mid + 1]
#             if mid - 1 < 0:
#                 return nums[0]
#             elif nums[mid] < nums[mid - 1]:
#                 return nums[mid]
            
#             if nums[mid] > nums[end]:
#                 start = mid + 1
#             else:
#                 end = mid - 1 

"""Optimal Textbook Approach"""
class Solution:
    def findMin(self, nums: list[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
                
        return nums[start]
    
"""
My version as well as the textbook version both are having almost similar time complexity in cases where the min value is close to mid my version gets completed sooner but my version has more cost
attached to it in each loop my version will always complete in 1 or 2 loop earlier but the running time of each loop is marginally higher although both are optimal versions.     
"""
        
obj = Solution()
nums = [45, 1, 3, 4, 6]
print(obj.findMin(nums))