
#include <iostream>
#include <vector>

class SudokuSolver {
public:
    std::vector<std::vector<char>> board;

    void solveSudoku(std::vector<std::vector<char>>& board) {
        this->board = std::move(board);
        solve();
        board = std::move(this->board);
    }

private:
    std::pair<int, int> findCellToFill() {
        for (int row = 0; row < 9; ++row)
            for (int col = 0; col < 9; ++col)
                if (board[row][col] == '.')
                    return {row, col};
        return {-1, -1};
    }

    bool solve() {
        auto [row, col] = findCellToFill();
        if (row == -1)
            return true;
        for (char num = '1'; num <= '9'; ++num) {
            if (isValid(row, col, num)) {
                board[row][col] = num;
                if (solve())
                    return true;
                board[row][col] = '.';
            }
        }
        return false;
    }

    bool isValid(int row, int col, char ch) {
        auto getRange = [](int x) { return std::vector<int>{x - x % 3, x - x % 3 + 1, x - x % 3 + 2}; };
        
        for (int i = 0; i < 9; ++i)
            if (board[row][i] == ch || board[i][col] == ch || board[getRange(row)[i/3]][getRange(col)[i%3]] == ch)
                return false;
        return true;
    }
};

int main() {
    std::vector<std::vector<char>> sudoku_board = {
        {'5','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}
    };

    SudokuSolver solver;
    solver.solveSudoku(sudoku_board);

    for (const auto& row : sudoku_board) {
        for (char cell : row)
            std::cout << cell << ' ';
        std::cout << '\n';
    }

    return 0;
}
