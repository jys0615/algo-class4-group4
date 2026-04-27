# 풀이를 작성하세요
import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
arr = [list(input().strip()) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    q = deque([(y, x)])
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<N and 0<=nx<N:
                if (arr[ny][nx] == '0' or arr[ny][nx] == 'E') and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[ey][ex] + 1
                    q.append((ny, nx))
                elif 'A' <= arr[ny][nx] <='F' and dist[ny][nx] == -1:
                    if (chr(ord(arr[ny][nx]) + 32)) in key:
                        dist[ny][nx] = dist[ey][ex] + 1
                        q.append((ny, nx))
                elif 'a' <= arr[ny][nx] <='f' and dist[ny][nx] == -1:
                    key.append(arr[ny][nx])
                    dist[ny][nx] = dist[ey][ex] + 1
                    q.append((ny, nx))
    return dist[end[0]][end[1]]




key = []
for j in range(N):
    for i in range(N):
        if arr[j][i] == 'S':
            start = j, i
        elif arr[j][i] == 'E':
            end = j, i
dist = [[-1]*N for _ in range(N)]
dist[start[0]][start[1]] = 0

print(bfs(start[0], start[1]))