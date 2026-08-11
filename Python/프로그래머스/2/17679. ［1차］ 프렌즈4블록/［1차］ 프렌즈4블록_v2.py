def solution(m, n, board):
    # 1. 처리를 편하게 하기 위해 행과 열을 바꿉니다 (Transpose)
    # 이제 각 행(row)이 원래의 열(column)이 되어, 중력 처리가 쉬워집니다.
    b = [list(row) for row in zip(*board)] # b[i][j]는 원래 board[j][i]에 해당함
    answer = 0

    while True:
        matched = set()
        # 2. 2x2 탐색 (회전된 보드 기준이므로 인덱스 주의)
        # b[i][j]는 원래 board[j][i]에 해당함
        for i in range(n - 1):
            for j in range(m - 1):
                if b[i][j] != '0' and b[i][j] == b[i+1][j] == b[i][j+1] == b[i+1][j+1]:
                    matched.update({(i, j), (i+1, j), (i, j+1), (i+1, j+1)})

        if not matched:
            break

        # 3. 일괄 제거 및 카운팅
        answer += len(matched)
        for i, j in matched:
            b[i][j] = '0'

        # 4. 중력 처리 (Pythonic!)
        # 각 행에서 '0'을 다 빼고, 뺀 만큼 앞쪽에 '0'을 채워넣습니다.
        for i in range(n):
            new_row = [c for c in b[i] if c != '0']
            b[i] = ['0'] * (m - len(new_row)) + new_row

    return answerc
