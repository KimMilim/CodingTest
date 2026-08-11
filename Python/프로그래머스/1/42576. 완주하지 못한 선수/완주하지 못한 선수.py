from collections import Counter

def solution(participant, completion):
    # 각 이름의 빈도수를 계산 (예: {'철수': 2, '영희': 1})
    answer = Counter(participant) - Counter(completion)
    
    # 남은 객체의 키(이름)를 반환
    return list(answer.keys())[0]