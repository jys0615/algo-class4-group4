import sys
INF = sys.maxsize

def solution(n, s, a, b, fares): # 지점갯수, 지점(s, a, b), fares(c, d, f) : c-> d 요금 f원
    answer = 0
    arr = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        arr[i][i] = 0
    for fare in fares:
        c, d, g = fare[0], fare[1], fare[2]
        arr[c][d] = g
        arr[d][c] = g

    for k in range(1, n+1): # 거치는 값
        for j in range(1, n+1): # 시작
            for i in range(1, n+1): # 도착
                if arr[j][i] > arr[j][k] + arr[k][i]:
                    arr[j][i] = arr[j][k] + arr[k][i]
    answer = float('inf')
    #### 보완할 점. 문제에 적힌 그대로 k를 기준으로 최소가 언제인지를 판별####
    for k in range(1, n+1): 
        answer = min(answer, arr[s][k]+arr[k][a]+arr[k][b])
    return answer