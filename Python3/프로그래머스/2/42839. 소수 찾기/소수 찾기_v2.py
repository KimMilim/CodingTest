from itertools import permutations

def is_prime(num):
    if num <=1:
        return False
    i=2
    while i <= int(num**0.5):
        if num%i==0:
            return False
        i+=1
    return True

def solution(numbers):
    
    res=set()
    
    for i in range(len(numbers)):
        res |= set(map(int, map("".join,permutations(numbers,i+1))))
        
    ans = sum(1 for ele in res if is_prime(ele))
    
    return ans
