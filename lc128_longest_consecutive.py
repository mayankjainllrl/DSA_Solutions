class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        print(num_set)
        longest_consecutive = 0
        for num in num_set:
            if num - 1 not in num_set:
                if num + longest_consecutive in num_set:
                    num_i = num
                    current_consecutive = 0
                    while num_i in num_set:
                        current_consecutive += 1
                        num_i += 1
                    if current_consecutive > longest_consecutive:
                        longest_consecutive = current_consecutive
        return longest_consecutive
        
        
sol = Solution()
nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, 6]
nums = [1,2,6,7,8]
nums2 = [0,3,7,2,5,8,4,6,0,1]
nums3 = [0, 54, 2, 1,2, 3, 4, 5, 6, 7, 8]
print(sol.longestConsecutive(nums))