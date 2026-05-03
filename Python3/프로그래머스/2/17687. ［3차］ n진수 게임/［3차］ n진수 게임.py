alpha = {10:'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15:'F'}

def transform_k(n,k):
    if n==0: return "0"
    res=""
    while n:
        if n%k >= 10:
            res = alpha[n%k]+res
        else: 
            res = str(n%k) + res
        n//=k
    
    # print(res)
    return res.lstrip('0')

def solution(n, t, m, p):
    answer = ""
    tmp=""
    
    i=0
    while True:
        res = transform_k(i,n)
        tmp += res
        if len(tmp) >= t*m: 
            break
        i+=1
    
    answer="".join([tmp[i] for i in range(len(tmp)) if i%m ==(p-1)])
    
    
    return answer[:t]