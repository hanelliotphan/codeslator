#include <iostream>
#include <vector>
#include <algorithm>

class SudokuSolver {
private:
    std::vector<std::vector<char>> board;

public:
    void solveSudoku(std::vector<std::vector<char>>& board) {
        this->board = board;
        solve();
        board = this->board;
    }

private:
    std::pair<int, int> findCellToFill() {
        for (int row = 0; row < 9; ++row) {
            for (int col = 0; col < 9; ++col) {
                if (board[row][col] == '.') {
                    return {row, col};
                }
            }
        }
        return {-1, -1};
    }

    bool solve() {
        auto [row, col] = findCellToFill();
        if (row == -1 && col == -1) return true;

        for (char num = '1'; num <= '9'; ++num) {
            if (isValid(row, col, num)) {
                board[row][col] = num;
                if (solve()) return true;
                board[row][col] = '.';
            }
        }
        return false;
    }

    bool isValid(int row, int col, char ch) {
        return isRowValid(row, ch) && isColValid(col, ch) && isSquareValid(row, col, ch);
    }

    bool isRowValid(int row, char ch) {
        return std::none_of(board[row].begin(), board[row].end(), [ch](char c) { return c == ch; });
    }

    bool isColValid(int col, char ch) {
        return std::none_of(board.begin(), board.end(), [col, ch](const auto& row) { return row[col] == ch; });
    }

    bool isSquareValid(int row, int col, char ch) {
        int startRow = row - row % 3, startCol = col - col % 3;
        for (int r = 0; r < 3; ++r) {
            for (int c = 0; c < 3; ++c) {
                if (board[startRow + r][startCol + c] == ch) return false;
            }
        }
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
        for (char c : row) {
            std::cout << c << ' ';
        }
        std::cout << '\n';
    }

    return 0;
}