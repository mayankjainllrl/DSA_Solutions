class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        pos_last = len(height) - 1
        pos_first = 0
        while pos_first < pos_last:
            distance = pos_last - pos_first
            if height[pos_first] < height[pos_last]:
                current_area = distance * height[pos_first]
                pos_first += 1
            else:
                current_area = distance * height[pos_last]
                pos_last -= 1
            
            max_area = max(current_area, max_area)
            
        return max_area
    

sol = Solution()
height = [3, 402, 2]
print(sol.maxArea(height))