def solution(name):
    n = len(name)
    answer = 0
    
    # 1) 상하 이동 비용: 각 글자별로 독립적으로 계산
    for ch in name:
        answer += min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)
    
    # 2) 좌우 이동 비용: 세 가지 전략 중 최솟값
    move = n - 1  # 전략 A: 그냥 오른쪽으로 끝까지
    
    for i in range(n):
        # i 이후 연속된 A 구간의 끝(다음 위치) 찾기
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        
        # 전략 B: 오른쪽으로 i까지 갔다가 되돌아와서 왼쪽으로 wrap
        # 전략 C: 왼쪽으로 wrap 먼저 갔다가 되돌아와서 오른쪽으로 i까지
        move = min(move,
                   2 * i + (n - next_i),       # B
                   i + 2 * (n - next_i))       # C
    
    return answer + move

