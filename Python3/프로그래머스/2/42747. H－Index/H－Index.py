def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    c_max = max(citations[0], len(citations))
    for h in range(c_max, -1,-1):
        cnt = sum(1 for c in citations if c>=h)
        if cnt >= h:
            answer=h
            break
    
    
    return answer