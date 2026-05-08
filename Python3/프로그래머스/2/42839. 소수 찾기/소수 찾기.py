def is_prime(num):
    if num <=1:
        return False
    i=2
    while i <= num**0.5:
        if num%i==0:
            return False
        i+=1
    return True

res_set=set()
def make_number(cur, numbers, visit):

    if cur and is_prime(int(cur)):
        global res_set
        res_set.add(int(cur))
        
    if sum(visit)==len(numbers): return
    
    for i in range(len(numbers)):
        if visit[i]: continue
        visit[i]=1
        make_number(cur+str(numbers[i]),numbers, visit)
        visit[i]=0
    
    return


def solution(numbers):
    
    visit = [0]*len(numbers)
    make_number("",numbers, visit)
    
    return len(res_set)