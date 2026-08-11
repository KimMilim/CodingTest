def solution(m, n, puddles):
    board = [[0 for _ in range(m+1)] for _ in range(n+1)]

    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [i,j] ==[1,1]: 
                board[i][j] = 1
                continue
            if [j,i] in puddles:
                continue
            board[i][j] = (board[i-1][j]+board[i][j-1])%1000000007
    
    for row in board:
        print(row)
    
    return board[n][m]%1000000007