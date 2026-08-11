def solution(dartResult):
    answer = 0
    
    cnt=0
    score=[]
    
    sdt="SDT"
    
    
    i=0
    while i< len(dartResult):
        c = dartResult[i]
        if c.isdigit():
            cnt+=1
            if i+1 < len(dartResult) and dartResult[i+1].isdigit():
                score.append(10)
                i+=1
            else:
                score.append(int(c))
        
        
        elif c in sdt:
            if c=='D':
                score[cnt-1] = score[cnt-1]**2
            if c=='T':
                score[cnt-1] = score[cnt-1]**3
        else:
            if c=='*':
                if cnt > 1:
                    score[cnt-2] = score[cnt-2] *2
                score[cnt-1] = score[cnt-1] *2
            if c=='#':
                score[cnt-1] = score[cnt-1] *(-1)
        i+=1
            
    
    
    # for i in score:
    #     print(i)
    
    return sum(score)