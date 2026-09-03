# DAA Lab Exercise
# Topic 6 - Backtracking - Question 4


# Q3/Q4 Sudoku
def sudoku(board):
    def bt():
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    for x in "123456789":
                        if x not in board[r] and all(board[i][c]!=x for i in range(9)) and all(board[i][j]!=x for i in range(r//3*3,r//3*3+3) for j in range(c//3*3,c//3*3+3)):
                            board[r][c]=x
                            if bt():return True
                            board[r][c]="."
                    return False
        return True
    bt();return board
B=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print("T6 Q3:",sudoku([r[:] for r in B]))
print("T6 Q4:",sudoku([r[:] for r in B]))
