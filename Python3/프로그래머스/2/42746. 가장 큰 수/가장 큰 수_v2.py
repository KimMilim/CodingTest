from functools import cmp_to_key

def solution(numbers):
    str_num = list(map(str, numbers))
    
    def compare(a, b):
    # 예: "가장 큰 수" 문제 로직
    # a+b가 더 크면 a를 앞으로 보내고 싶음 (음수 반환)
        if a + b > b + a:
            return -1
        else:
            return 1
    
    # str_num.sort(key=cmp_to_key(compare))
    str_num.sort(key=cmp_to_key(lambda a,b: -1 if a+b> b+a else 1))
    
    # 3. 정렬된 결과 합치기
    answer = "".join(str_num)
    
    # 4. "000" 같은 경우 "0"만 리턴하도록 예외 처리
    return "0" if int(answer)==0 else answer
