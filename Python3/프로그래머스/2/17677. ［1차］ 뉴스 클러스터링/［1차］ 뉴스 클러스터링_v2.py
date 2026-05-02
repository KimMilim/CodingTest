from collections import Counter

def solution(str1, str2):
    # 1. 리스트 컴프리헨션으로 다중집합 생성
    list1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    list2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    # 2. Counter를 이용한 빈도수 계산
    c1 = Counter(list1)
    c2 = Counter(list2)
    
    # 3. Counter의 교집합(&)과 합집합(|) 연산 활용
    # elements()는 빈도수만큼 요소를 반복하는 이터레이터를 반환합니다.
    inter_len = sum((c1 & c2).values())
    union_len = sum((c1 | c2).values())
    
    # 4. 예외 처리 및 결과 계산
    if union_len == 0:
        return 65536
    
    return int((inter_len / union_len) * 65536)
