# Problem: https://leetcode.com/problems/sudoku-solver/description/
# Solution's Author: Han-Elliot Phan (hanelliotphan@gmail.com)
# Solution Year: 2020

class SudokuSolver:
    def solveSudoku(self, board) -> None:
        self.board = board
        self.solve()
        
    
    def findCellToFill(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1
        
    
    def solve(self):
        row, col = self.findCellToFill()
        if (row, col) == (-1, -1):
            return True  
        for num in map(str, range(1, 10)):
            if self.isValid(row, col, num):
                self.board[row][col] = num
                
                if self.solve():
                    return True
                self.board[row][col] = '.'
        
    
    def isValid(self, row, col, ch):
        is_row_valid = all(self.board[row][_] != ch for _ in range(9))
        is_col_valid = all(self.board[_][col] != ch for _ in range(9))   
        is_square_valid = all(self.board[r][c] != ch for r in self.getRange(row) for c in self.getRange(col))
        return is_row_valid and is_col_valid and is_square_valid 
    
    
    def getRange(self, x):
        x -= x % 3
        return range(x, x + 3)

sudoku_board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solver = SudokuSolver()
solver.solveSudoku(sudoku_board)
print(solver.board)
