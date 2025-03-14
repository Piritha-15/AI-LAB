print("Enter the number of queens")
N = int(input())

board = [[0] * N for _ in range(N)]

def is_safe(i, j):
    for k in range(N):
        if board[i][k] == 1 or board[k][j] == 1:
            return False

    for k in range(N):
        for l in range(N):
            if (k + l == i + j or k - l == i - j) and board[k][l] == 1:
                return False

    return True

def solve_n_queens(n):
    if n == 0:
        return True

    for i in range(N):
        for j in range(N):
            if not is_safe(i, j):
                continue

            if board[i][j] != 1:
                board[i][j] = 1
                if solve_n_queens(n - 1):
                    return True
                board[i][j] = 0  

    return False
if solve_n_queens(N):
    print("Solution exists. Placements of queens:")
    for row in board:
        print(row)
else:
    print("No solution exists.")