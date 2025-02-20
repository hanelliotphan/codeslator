
import java.util.Arrays;

public class SudokuSolver {

    private char[][] board;

    public void solveSudoku(char[][] board) {
        this.board = board;
        solve();
    }

    private boolean solve() {
        int[] cell = findCellToFill();
        int row = cell[0], col = cell[1];
        if (row == -1) return true;
        for (char num = '1'; num <= '9'; ++num) {
            if (isValid(row, col, num)) {
                board[row][col] = num;
                if (solve()) return true;
                board[row][col] = '.';
            }
        }
        return false;
    }

    private int[] findCellToFill() {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                if (board[row][col] == '.') return new int[]{row, col};
            }
        }
        return new int[]{-1, -1};
    }

    private boolean isValid(int row, int col, char ch) {
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == ch || board[i][col] == ch || board[row / 3 * 3 + i / 3][col / 3 * 3 + i % 3] == ch) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        char[][] sudokuBoard = {
            {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
            {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
            {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
            {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
            {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
            {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
            {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
            {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
            {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };
        SudokuSolver solver = new SudokuSolver();
        solver.solveSudoku(sudokuBoard);
        for (char[] row : sudokuBoard) {
            System.out.println(Arrays.toString(row));
        }
    }
}
