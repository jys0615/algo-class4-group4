import math
def solution(fees, records):
    answer = dict()
    basic_time = fees[0] # 기본 시간
    basic_fee = fees[1] # 기본 요금(원)
    unit_time = fees[2] # 단위 시간(분)
    unit_fee = fees[3] # 단위 요금(원)
    for record in records:
        t, num, rs = record.split()
        answer[num] = 0
    for record in records:
        t, num, rs = record.split()
        h, m = t.split(":")
        time = 60*int(h)+int(m) # HH:MM -> MM으로 변환
        if rs == "IN":
            answer[num]-=time
        else:
            answer[num]+=time
    for key, value in answer.items():
        if value <= 0:
            answer[key]+=23*60+59
    number = sorted(answer.keys(), key = lambda x : x) # key값들을 오름차순 정렬.
    
    result = []
    for num in number: # 정렬된 키값 순서대로 주차 요금 계산
        if answer[num] <= basic_time:
            result.append(basic_fee)
        else:
            result.append(basic_fee + math.ceil((answer[num] - basic_time) / unit_time) * unit_fee)
    return result