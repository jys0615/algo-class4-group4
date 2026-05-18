"""
1. 아이디어
- "시작점이 여러 개"일 때 큐에 전부 넣고 동시에 BFS 시작
- 각 칸까지 가장 가까운 시작점의 거리를 구함
2. 시간복잡도
- BFS : O(N*M)
3. 자료구조
- 지도 : int[][]
- 거리 : int[][] dist (-1 초기화)
- Queue(BFS)
"""

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
dist = [[0-1]*m for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

q = deque()

for j in range(n):
    for i in range(m):
        if mp[j][i] == 1:
            q.append((j, i))
            dist[j][i] = 0
while q:
    ey, ex = q.popleft()
    for k in range(4):
        ny = ey + dy[k]
        nx = ex + dx[k]
        if 0<=ny<n and 0<=nx<m:
            if dist[ny][nx] == -1:
                dist[ny][nx] = dist[ey][ex] + 1
                q.append((ny, nx))

                