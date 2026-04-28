from math import ceil

def solution(n, stations, w):
    cnt = 0
    # 가상 경계: 왼쪽 끝(0), 오른쪽 끝(n+1) 추가
    # stations는 1-indexed 그대로 사용
    
    left = 1  # 현재 탐색 시작점
    
    for s in stations:
        # s 기지국의 커버 시작점
        right = s - w - 1  # 빈 구간의 오른쪽 끝
        
        gap = right - left + 1  # 빈 구간 길이
        if gap > 0:
            cnt += ceil(gap / (2 * w + 1))
        
        left = s + w + 1  # 다음 탐색 시작점
    
    # 마지막 기지국 이후 ~ n까지 처리
    gap = n - left + 1
    if gap > 0:
        cnt += ceil(gap / (2 * w + 1))
    
    return cnt
### 시간 초과 발생 ###
# from math import ceil
# def solution(n, stations, w):
#     result = [0]*n
#     for item in stations:
#         result[item-1] = 1
#         for i in range(1, w+1):
#             if 0<=item-1-i<n:
#                 result[item-1-i] = 1
#             if 0<=item-1+i<n:
#                 result[item-1+i] = 1
    
#     # print(result)
#     answer = [[] for _ in range(n)]
#     cnt = 0
#     length = 0
    
#     for i, item in enumerate(result):
#         if item == 0: # 0이 연속되는 것을 계속 측정
#             length += 1
#         else:
#             cnt += ceil(length / (2*w+1)) # 1이 나온다면 지금까지 0의 길이에 대해 기지국 개수 세기
#             length = 0
            
#     cnt += ceil(length / (2*w+1))
    
#     return cnt