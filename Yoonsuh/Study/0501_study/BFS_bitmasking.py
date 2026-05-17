"""
1. 아이디어
- 방문 상태를 비트로 표현
- chk[y][x][state] : y, x 위치에서 state 상태로 방문
- state : 비트마스크로 어떤 아이템을 획득했는지 표현
2. 시간복잡도
- O(N * M * 2^K) : K = 아이템 종류 수
3. 자료구조
- 지도 : int[][]
- 방문 : bool[][][2^K] chk
- Queue(BFS) : (y, x, state)
"""
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mp = [list(input().strip()) for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 아이템 위치 수집
items = {}
cnt = 0
for j in range(n):
    for i in range(m):
        if mp[j][i] == 'K':
            items[(j, i)] = cnt
            cnt += 1

full = (1 << cnt) - 1
chk = [[[False]*(1<<cnt) for _ in range(m)] for _  in range(n)]

sy, sx = 0, 0
q = deque([(sy, sx, 0)])
chk[sy][sx][0] = True
step = 0

while q:
    for _ in range(len(q)):
        ey, ex, state = q.popleft()
        if state == full:
            print(step)
            exit()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m and mp[ny][nx] != '#':
                nstate = state
                if (ny, nx) in items:
                    nstate |= (1 << items[(ny, nx)])
                if not chk[ny][nx][nstate]:
                    chk[ny][nx][nstate] = True
                    q.append((ny, nx, nstate))
        step += 1