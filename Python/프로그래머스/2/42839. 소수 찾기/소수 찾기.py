from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    # 2부터 루트 n까지 나누어 떨어지는지 확인
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    candidate_numbers = set()
    
    # 1. 1개부터 len(numbers)개까지 뽑는 모든 순열을 구함
    for i in range(1, len(numbers) + 1):
        permu = permutations(numbers, i)
        
        # 2. 각 순열 글자들을 합쳐서 숫자로 변환 후 set에 저장 (중복 자동 제거)
        for p in permu:
            num = int("".join(p))
            candidate_numbers.add(num)
            
    # 3. set에 담긴 고유한 숫자들 중 소수의 개수를 카운트
    answer = 0
    for num in candidate_numbers:
        if is_prime(num):
            answer += 1
            
    return answer