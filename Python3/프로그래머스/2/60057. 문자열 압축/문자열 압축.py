def solution(s):
    answer = 0
    
    min_s = s
    for i in range(1,len(s)//2+1):
        words=[]
        
        j=0
        while j < len(s):
            words.append(s[j:j+i])
            j+=i
        
        tmp=""
        pre=""
        cnt=0
        for w in words:
            if pre != w:
                if cnt > 1:
                    tmp+= (str(cnt)+pre)
                else:
                    tmp+= pre
                pre=w
                cnt=1
            else:
                cnt+=1
        if cnt > 1:
            tmp+= (str(cnt)+pre)
        else:
            tmp+= pre

        if len(tmp) < len(min_s):
            min_s=tmp
            # print(tmp)
                
        
    return len(min_s)