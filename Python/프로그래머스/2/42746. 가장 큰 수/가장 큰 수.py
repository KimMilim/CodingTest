from functools import cmp_to_key

def solution(numbers):
    str_num = list(map(str, numbers))
    
    # 2. 커스텀 정렬: a+b와 b+a를 비교
    # a+b가 더 크면 a가 앞에 오도록(내림차순 느낌) 설정
    str_num.sort(key=cmp_to_key(lambda a, b: -1 if a + b > b + a else 1))
    
    # 3. 정렬된 결과 합치기
    answer = "".join(str_num)
    
    # 4. "000" 같은 경우 "0"만 리턴하도록 예외 처리
    return "0" if int(answer)==0 else answer