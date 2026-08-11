def transfrom_k(n,k):
    res = ""
    while n:
        res = str(n%k)+res
        n//=k
    return res

def IsPrime(str_n):
    n = int(str_n)
    if n <= 1: return False
    
    i=2
    while i*i <= n:
        if n%i==0:
            return False
        i+=1
    return True

def solution(n, k):
    answer = 0
    
    res = transfrom_k(n,k)
    
    tmp=""
    for c in res:
        if c =='0':
            if tmp!="" and IsPrime(tmp):
                answer+=1
                # print("case1:", tmp)
            tmp=""
        elif c!='0':
            tmp+=c
            # print("case2:", tmp)
    
    if tmp!="" and IsPrime(tmp):
        answer+=1
        
    return answer