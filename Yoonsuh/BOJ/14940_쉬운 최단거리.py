import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [[-1]*m for _ in range(n)] # 전부 -1로 초기화 => 만약 갈 수 있는 곳인데 도달 못하면 그대로 -1
dy = [-1,0,1,0]
dx = [0,1,0,-1]
def bfs(y, x):
    q = deque([(y, x)])
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey+dy[k]
            nx = ex+dx[k]
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] == 1 and result[ny][nx] == -1:
                    result[ny][nx] = result[ey][ex]+1 # 현재 위치는 이전 위치에서 +1
                    q.append((ny, nx))


for j in range(n):
    for i in range(m):
        if arr[j][i] == 2:
            start = j, i
result[start[0]][start[1]] = 0 ### 중요!!! 테스트 입력에 (0,0)이라고 하드코딩을 하면 안 됨. 시작 위치는 유동적
bfs(start[0], start[1]) # 시작 지점을 기준으로 이동 시작

for j in range(n): 
    for i in range(m):
        if arr[j][i] == 0: # 원래 갈 수 없는 땅은
            result[j][i] = 0 # 0으로 출력
for item in result:
    print(*item)