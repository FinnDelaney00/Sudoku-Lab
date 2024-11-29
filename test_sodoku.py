import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import unittest
from sodoku import solve_sudoku

class TestSudokuSolver(unittest.TestCase):

    def is_valid_sudoku(self, board):
        """Helper function to check if the Sudoku board is valid"""
        for i in range(9):
            # Check if all rows contain unique numbers from 1 to 9 (ignore 0)
            if len(set(board[i])) != len([x for x in board[i] if x != 0]):
                return False
            # Check if all columns contain unique numbers from 1 to 9 (ignore 0)
            if len(set(board[j][i] for j in range(9))) != len([board[j][i] for j in range(9) if board[j][i] != 0]):
                return False
            # Check 3x3 subgrids
            row_start = (i // 3) * 3
            col_start = (i % 3) * 3
            subgrid = [board[row_start + r][col_start + c] for r in range(3) for c in range(3)]
            if len(set(subgrid)) != len([x for x in subgrid if x != 0]):
                return False
        return True

    def test_valid_easy(self):
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        solution = solve_sudoku(board)
        self.assertIsNotNone(solution)
        self.assertTrue(self.is_valid_sudoku(solution))

    def test_valid_medium(self):
        board = [
            [8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 6, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 9, 0, 2, 0, 0],
            [0, 5, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 4, 5, 7, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 0, 0, 6, 8],
            [0, 0, 8, 5, 0, 0, 0, 1, 0],
            [0, 9, 0, 0, 0, 0, 4, 0, 0]
        ]
        solution = solve_sudoku(board)
        self.assertIsNotNone(solution)
        self.assertTrue(self.is_valid_sudoku(solution))

    def test_unsolvable(self):
        board = [
            [5, 5, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        solution = solve_sudoku(board)
        self.assertIsNone(solution)

    def test_invalid_input(self):
        board = [
            [5, 3, 0, 0],  # Invalid dimensions
        ]
        with self.assertRaises(ValueError):
            solve_sudoku(board)

    def test_empty_sudoku(self):
        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        solution = solve_sudoku(board)
        self.assertIsNotNone(solution)
        self.assertTrue(self.is_valid_sudoku(solution))

    def test_single_value_sudoku(self):
        board = [
            [5, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        solution = solve_sudoku(board)
        self.assertIsNotNone(solution)
        self.assertTrue(self.is_valid_sudoku(solution))


if __name__ == "__main__":
    unittest.main()
