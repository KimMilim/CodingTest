def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    res = ''
    while n:
        res = str(n % k) + res
        n //= k
    
    # ['11', '', '11'] --> 필터링 필요
    candidates = [int(v) for v in res.split('0') if v]
    
    return sum(1 for cand in candidates if is_prime(cand))
