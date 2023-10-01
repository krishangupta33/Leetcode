def solveSudoku(board):
    # check if the board is valid
    def isValid(board, row, col, c):
        for i in range(9):
            if board[i][col] != '.' and board[i][col] == c: return False
            if board[row][i] != '.' and board[row][i] == c: return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3] != '.' and board[3*(row//3)+i//3][3*(col//3)+i%3] == c: return False
        return True
    
    def solve(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in '123456789':
                        if isValid(board, i, j, c):
                            board[i][j] = c
                            if solve(board): return True
                            else: board[i][j] = '.'
                    return False
        return True
    
    solve(board)
    
    return board







input = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

print(solveSudoku(input))

