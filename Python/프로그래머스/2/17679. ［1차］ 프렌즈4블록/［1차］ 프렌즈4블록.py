
dir = [[0,0],[0,1],[1,0],[1,1]]

def solution(m, n, board):
    answer = 0
    
    
    numboard = [['0' for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            numboard[i][j] = board[i][j]
    
    # sum=0
    while True:
        cnt=0
        # if sum >= 20: break
        # sum+=1
        candidate=set()
        for i in range(m-1):
            for j in range(n-1):
                block = numboard[i][j]
                if block=='0': continue
                
                if numboard[i+1][j] == block and numboard[i][j+1] == block and numboard[i+1][j+1] == block:
                    # print(i,j)
                    for d in range(4):
                        dr = i+dir[d][0]
                        dc = j+dir[d][1]
                        candidate.add((dr,dc))
                    
        if len(candidate)==0:
            break
        answer += len(candidate)
        
        for r,c in candidate:
            numboard[r][c]='0'
        
        
        
        newboard = [['0' for _ in range(n)] for _ in range(m)]
        for j in range(n):
            ii=m-1
            for i in range(m-1,-1,-1):
                if numboard[i][j]!='0':
                    newboard[ii][j]=numboard[i][j]
                    ii-=1
        numboard = newboard
        
        
        # for row in numboard:
        #     print(row)
        # print()
                
        
    
    return answer