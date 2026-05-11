from itertools import groupby

def solution(s):
    n = len(s)
    if n == 1:
        return 1
    
    def compressed_length(size):
        # 1) size 크기로 자르기
        chunks = [s[i:i+size] for i in range(0, n, size)]
        
        # 2) 연속된 같은 조각을 그룹핑해서 압축
        parts = []
        for chunk, group in groupby(chunks):
            count = sum(1 for _ in group)
            parts.append(f"{count}{chunk}" if count > 1 else chunk)
        
        return len(''.join(parts))
    
    return min(compressed_length(size) for size in range(1, n // 2 + 1))