
import 'dart:io';

class SudokuSolver {
  late List<List<String>> board;

  void solveSudoku(List<List<String>> board) {
    this.board = board;
    solve();
  }

  (int, int) findCellToFill() {
    for (int row = 0; row < 9; row++) {
      for (int col = 0; col < 9; col++) {
        if (board[row][col] == '.') {
          return (row, col);
        }
      }
    }
    return (-1, -1);
  }

  bool solve() {
    final (row, col) = findCellToFill();
    if (row == -1 && col == -1) return true;
    
    for (String num in List.generate(9, (i) => (i + 1).toString())) {
      if (isValid(row, col, num)) {
        board[row][col] = num;
        if (solve()) return true;
        board[row][col] = '.';
      }
    }
    return false;
  }

  bool isValid(int row, int col, String ch) {
    return board[row].every((cell) => cell != ch) &&
           List.generate(9, (i) => board[i][col]).every((cell) => cell != ch) &&
           getRange(row).every((r) => getRange(col).every((c) => board[r][c] != ch));
  }

  Iterable<int> getRange(int x) sync* {
    x -= x % 3;
    yield x;
    yield x + 1;
    yield x + 2;
  }
}

void main() {
  final sudokuBoard = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
  ];

  final solver = SudokuSolver();
  solver.solveSudoku(sudokuBoard);
  print(solver.board);
}
