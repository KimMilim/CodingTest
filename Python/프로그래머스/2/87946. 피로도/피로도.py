def solution(k, dungeons):
    answer = 0
    
    
    def solve(cur_k, visit, cnt):
        
        nonlocal answer
    
        if cnt > answer:
            answer = cnt
        
        for i in range(len(dungeons)):
            if visit[i] or cur_k < dungeons[i][0]:
                continue
            
            visit[i]=True
            solve(cur_k-dungeons[i][1], visit, cnt+1)
            visit[i]=False
    
        return

    visit = [False for i in range(len(dungeons))]
    solve(k,visit, 0)
    
    
    return answer