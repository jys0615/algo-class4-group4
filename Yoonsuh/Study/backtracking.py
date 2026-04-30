"""
백트래킹 : 선택 -> 탐색 -> 취소

<백트래킹 문제의 뼈대>
def recur(현재상태):
if 목표달성:
    결과저장
    return

    for 선택지 in 가능한선택들:
        선택하기
        recur(다음상태)
        선택취소
"""

"""
1. 아이디어
- 1~N 중 M개 순열
- chk로 이미 선택한 거 표시
- M개 선택되면 출력

2. 시간복잡도
- O(N!) > N 작으면 가능

3. 자료구조
- 결과값 rs : int[]
- 방문여부 chk : bool[]
"""

# import sys
# input = sys.stdin.readline

# N, M = 4, 2
# rs = []
# chk = [False] * (N+1)

# def recur():
#     if len(rs) == M:
#         print(rs)
#         return
#     for i in range(1, N+1):
#         if chk[i] == False:
#             chk[i] = True
#             rs.append(i)
#             recur()
#             rs.pop()
#             chk[i] = False

# recur()

"""
1. 아이디어
-  모든 던전 순서 시도 (순열)
- 현재 피로도로 입장 가능하면 탐험
- 최대 탐험 수 갱신

2. 시간복잡도 
- O(N!) N<=8 > 가능

3. 자료구조
- 방문여부 chk : bool[]
- 최대탐험수 maxv : int
"""
import sys
input = sys.stdin.readline

def solution(k, dungeons):
    N = len(dungeons)
    chk = [False] * N
    maxv = 0

    def recur(tired, cnt):
        nonlocal maxv
        maxv = max(maxv, cnt)

        for i in range(N):
            if chk[i] == False and dungeons[i][0] <= tired:
                chk[i] = True
                recur(tired - dungeons[i][1], cnt+1)
                chk[i] = False
        recur(k, 0)
        return maxv
