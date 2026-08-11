from collections import Counter

def solution(str1, str2):
    
    list1=[str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha() ]
    list2=[str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha() ]
    
    c1 = Counter(list1) # ['aa', 'aa', 'bb']였다면 {'aa': 2, 'bb': 1}
    c2 = Counter(list2)

    inter_len = sum((c1 & c2).values()) # c1 = {'aa': 2, 'bb': 1}, c2 = {'aa': 3, 'bb': 0} 이라면 c1 & c2는 {'aa': 2}
    union_len = sum((c1 | c2).values()) # c1 | c2는 {'aa': 3, 'bb': 1}
    
    
    if union_len == 0:
        return 65536
    
    return int((inter_len / union_len) * 65536)
