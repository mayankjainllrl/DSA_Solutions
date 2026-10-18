class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        solution_pairs = []
        prev_num = None
        for i, num in enumerate(nums[:-2]):
            if num > 0:
                break
            if prev_num == num:
                continue
            prev_num = num
            start = i + 1
            end = len(nums) - 1
            prev_inner_start = None
            prev_inner_end = None
            while start < end:
                if prev_inner_start == nums[start]:
                    start += 1
                    continue
                if prev_inner_end == nums[end]:
                    end -= 1
                    continue 
                sum_of_three = nums[start] + nums[end] + num
                if sum_of_three == 0:
                    solution_pairs.append([num, nums[start], nums[end]])
                    start += 1
                    end -= 1
                elif sum_of_three < 0:
                    start += 1
                else:
                    end -= 1
                prev_inner_start = nums[start]
                prev_inner_end = nums[end]

        return solution_pairs
    
sol = Solution()
nums = [1,2,0,1,0,0,0,0]
print(sorted(nums))
print(sol.threeSum(nums))