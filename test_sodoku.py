import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import unittest
from sodoku import solve_sudoku

class TestSudokuSolver(unittest.TestCase):
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
        self.assertEqual(solution, [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ])

    def test_unsolvable(self):
        board = [
            [5, 5, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            # Incomplete board for illustration
        ]
        self.assertIsNone(solve_sudoku(board))

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
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.assertIsNone(solve_sudoku(board))

    def test_single_value_sudoku(self):
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
        result = solve_sudoku(board)
        self.assertIsNone(result)

    def test_valid_medium(self):
        board = [
            [8, 1, 2, 0, 5, 3, 0, 4, 9],
            [9, 4, 3, 0, 8, 2, 1, 7, 5],
            [1, 5, 0, 0, 9, 0, 0, 8, 3],
            [6, 7, 5, 4, 9, 1, 2, 8, 3],
            [2, 3, 1, 7, 5, 0, 0, 9, 6],
            [4, 9, 0, 3, 1, 6, 7, 5, 2],
            [7, 0, 0, 9, 4, 8, 6, 3, 1],
            [5, 2, 9, 1, 3, 7, 8, 6, 4],
            [3, 6, 8, 2, 7, 5, 9, 1, 0]
        ]
        solution = solve_sudoku(board)
        self.assertEqual(solution, [
            [8, 1, 2, 6, 5, 3, 7, 4, 9],
            [9, 4, 3, 8, 2, 7, 1, 5, 6],
            [1, 5, 7, 4, 9, 6, 2, 8, 3],
            [6, 7, 5, 4, 9, 1, 2, 8, 3],
            [2, 3, 1, 7, 5, 9, 4, 9, 6],
            [4, 9, 2, 8, 3, 6, 7, 5, 2],
        ])

if __name__ == '__main__':
    unittest.main()
