def solve(arr, n, r, c):
    cnt_0=0
    cnt_1=0
    
    for i in range(r,r+n):
        tmp = sum(arr[i][c:c+n])
        cnt_1 +=tmp
        cnt_0 += (n-tmp)
        
        if cnt_0 and cnt_1:
            break
    if cnt_0 == n*n:
        return [1,0]
    elif cnt_1 == n*n:
        return [0,1]
    
    
    half = n // 2
    parts = [
        solve(arr, half, r, c),
        solve(arr, half, r, c + half),
        solve(arr, half, r + half, c),
        solve(arr, half, r + half, c + half),
    ]
    
    res = [0,0]
    for p in parts:
        res[0] += p[0]
        res[1] += p[1]
        
    
    return res


def solution(arr):
    return solve(arr, len(arr), 0, 0)