from collections import deque

def solution(n, edge):
    answer = 0
    
    INF=123456789
    
    dist = [INF] * (n+1)
    adj = [[] for i in range(n+1)]
    
    for l in edge:
        v1,v2 = l
        adj[v1].append(v2)
        adj[v2].append(v1)
    
    
    deq = deque()
    dist[1]=0
    
    deq.append([1,0])
    
    while deq:
        
        cur = deq.pop()
        for next in adj[cur[0]]:
            if dist[next] > cur[1]+1:
                dist[next] = cur[1]+1
                deq.append([next,dist[next]])
        
    max_d = max(dist[1:])
    
    return sum(1 for i in dist if i==max_d)