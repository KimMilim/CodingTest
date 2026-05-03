def solution(n, t, m, p):
    digits = "0123456789ABCDEF"
    
    full_string = "0"
    num = 1
    
    while len(full_string) < t * m:
        tmp = ""
        cur = num
        while cur > 0:
            tmp = digits[cur % n] + tmp
            cur //= n
        full_string += tmp
        num += 1
        
    return full_string[p-1 : t*m : m]
