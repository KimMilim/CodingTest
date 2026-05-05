
"""

2. 알파벳 대소, 스페이스, 숫자, 점, 빼기
3. 파일명 영문자로 시작, 숫자 하나이상 포함

- HEAD: 숫자가 아닌 문자만, 최소 1자 이상
- NUMBER: 1~5자의 숫자, 앞에 0이 올수 있음
- TAIL: 나머지 부분, "" 가능

정렬:
1. HEAD 기준 사전순(대소문자 구분 X)
2. NUMBER 숫자 오름차순(앞의 0은 무시)
3. 입력된 순
"""

import re

def solution(files):
    answer = []
    
    file_list=[]
    
    for file in files:
        tmp = re.findall(r"([^\d]+)(\d{1,5})(.*)", file) # ([^0-9]+)([0-9]{1,5})(.*) or ([^\d]+)(\d{1,5})(.*)
        if tmp:
            head, number, tail = tmp[0] # tmp는 2중 배열
            # print(head, number, tail)
            file_list.append((head, number, tail, file))
    
    file_list.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    for h,n,t,f in file_list:
        answer.append(f)
    
    return answer