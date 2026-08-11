from collections import deque

def solution(n, computers):
    answer = 0
    
    visit = [0]*(n)
    q = deque()
            
    def bfs(s):
        visit[s]=1
        q.append(s)
        
        while q:
            cur = q.pop()
            for j in range(len(computers[cur])):
                if computers[cur][j]==0 or visit[j]: continue
                
                visit[j]=1
                q.append(j)
        
    for i in range(n):
        if not visit[i]:
            bfs(i)
            answer+=1
    
    return answer