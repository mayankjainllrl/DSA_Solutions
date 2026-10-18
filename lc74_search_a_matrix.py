
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        i, j = len(matrix), len(matrix[0])
        start_i, start_j = 0, 0
        end_i, end_j = i - 1, j - 1
        
        while start_i < end_i or (start_i == end_i and start_j <= end_j):
            mid_val = ((j - start_j) + (end_j + 1) + (end_i - start_i - 1) * j) // 2  
            current_row = mid_val - (j - start_j)
            if current_row < 0:
                mid_i = start_i
                mid_j = mid_val + start_j
            else:
                mid_i = (current_row // j) + start_i + 1
                mid_j = (current_row % j)
            
            if target == matrix[mid_i][mid_j]:
                return True
            elif target < matrix[mid_i][mid_j]:
                if mid_j - 1 < 0:
                    end_i = mid_i - 1
                    end_j = j - 1
                else:
                    end_i = mid_i
                    end_j = mid_j - 1
            else:
                if mid_j + 1 >= j:
                    start_i = mid_i + 1
                    start_j = 0
                else:
                    start_i = mid_i
                    start_j = mid_j + 1
        return False



sol = Solution()
matrix = [
    [1],
    [2],
    [3],
    [4],
    [5],
    [6]
]
target = 1
print(sol.searchMatrix(matrix, target))