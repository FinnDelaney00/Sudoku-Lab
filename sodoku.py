def is_valid_board(board):
    # Check board dimensions (9x9 grid)
    if len(board) != 9 or any(len(row) != 9 for row in board):
        return False
    # Check for valid numbers (0-9)
    for row in board:
        for num in row:
            if not (0 <= num <= 9):
                return False
    return True

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True  # No empty spaces, solution found
    row, col = empty

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_safe(board, row, col, num):
    # Check row
    if num in board[row]:
        return False
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False
    # Check 3x3 grid
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    # Validate input board dimensions
    if len(board) != 9 or any(len(row) != 9 for row in board):
        raise ValueError("Invalid board size. Board must be 9x9.")
    
    if not is_valid_board(board):
        raise ValueError("Invalid board")
    
    board_copy = [row[:] for row in board]  # Deep copy to avoid mutation
    if solve(board_copy):
        return board_copy
    return None
