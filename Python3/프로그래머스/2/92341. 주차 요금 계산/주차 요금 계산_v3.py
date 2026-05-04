import math
from collections import defaultdict

def transform(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def solution(fees, records):
    base_t, base_f, unit_t, unit_f = fees
    parking = {}        # 현재 주차 중인 차량 (차량번호: 입차시간)
    total_times = defaultdict(int) # 차량별 누적 시간 (차량번호: 총시간)

    # 1. 기록 처리
    for record in records:
        time_str, car, status = record.split()
        time = transform(time_str)
        
        if status == "IN":
            parking[car] = time
        else:
            # pop을 쓰면 가져옴과 동시에 삭제되므로 관리가 편합니다.
            total_times[car] += time - parking.pop(car)

    # 2. 출차 기록 없는 차량 일괄 처리
    limit_time = transform("23:59")
    for car, in_time in parking.items():
        total_times[car] += limit_time - in_time

    # 3. 요금 계산 (차량 번호 오름차순 정렬)
    answer = []
    for car in sorted(total_times.keys()):
        total_t = total_times[car]
        
        # 기본 요금 + 초과 시간 요금 (0보다 작아지지 않게 max 활용)
        extra_t = max(0, total_t - base_t)
        fee = base_f + math.ceil(extra_t / unit_t) * unit_f
        answer.append(fee)

    return answer
