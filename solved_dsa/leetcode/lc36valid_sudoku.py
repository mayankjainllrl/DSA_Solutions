from typing import List
from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def group_validator(line):
            counts = {}
            for i, num in enumerate(line):
                print(num)
                counts[num] = counts.get(num, 0) + 1
                if num != '.' and counts.get(num) > 1:
                    return False
            return True
        
        boxes = [[] for _ in range(9)]
        i_slicer = 0
        for i in range(9):
            if i >= 3:
                i_slicer = 3
            if i >= 6:
                i_slicer = 6
            j_slicer = 0
            j_start = 0
            for j in range(3, 10, 3):
                boxes[j_slicer + i_slicer] += board[i][j_start:j]
                j_slicer += 1
                j_start = j
                
        for i in range(9):
            if not group_validator(board[i]):
                return False
            if not group_validator([board[j][i] for j in range(9)]):
                return False
            if not group_validator(boxes[i]):
                return False
        
        return True
        


    
sudoku = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

sol = Solution()
for i, line in enumerate(sudoku):
    print(line)
print()
print(sol.isValidSudoku(sudoku))