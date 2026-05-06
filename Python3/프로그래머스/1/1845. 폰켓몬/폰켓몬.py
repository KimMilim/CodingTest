from collections import Counter

def solution(nums):
    answer = 0
    
    c = Counter(nums)
    
    if len(c) >= len(nums)//2:
        answer = len(nums)//2
    else:
        answer = len(c)
    
    return answer