import sys
from collections import deque

# 방향: 1:상, 2:하, 3:좌, 4:우
# dx, dy 매핑 (0은 사용하지 않음)
dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]

change_dir = [ # 각 방향에 따라 다른 dir을 활용한다. 
    [0, 0, 0, 0, 0],
    [0, 1, 3, 4, 2], 
    [0, 2, 4, 3, 1],
    [0, 3, 2, 1, 4],
    [0, 4, 1, 2, 3],
]

def solve():
    input_data = input().strip().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    r, c = int(input_data[1]) - 1, int(input_data[2]) - 1
    d = int(input_data[3])
    
    grid = []
    idx = 4
    for i in range(N):
        grid.append([int(x) for x in input_data[idx : idx + N]])
        idx += N
        
    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True
    print(f"{r + 1} {c + 1}")

    def explore():
        nonlocal r, c, d
        for i in range(1, 5):
            dir_val = change_dir[d][i]
            nr, nc = r + dy[dir_val], c + dx[dir_val]
            
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0 and not visited[nr][nc]:
                r, c, d = nr, nc, dir_val
                visited[r][c] = True
                return True
        return False

    def get_next_step():
        chk = [[False] * N for _ in range(N)]
        q = deque([(r, c, 0, 0)])  # r, c, dist, dir
        chk[r][c] = True
        
        candidates = []
        priority_dir = [3, 2, 4, 1] # 왼, 아래, 오른, 위 순으로 탐색 
        
        while q:
            cr, cc, dist, _ = q.popleft()
            
            for pd in priority_dir:
                nr, nc = cr + dy[pd], cc + dx[pd]
                
                if 0 <= nr < N and 0 <= nc < N and not chk[nr][nc] and grid[nr][nc] == 0:
                    chk[nr][nc] = True
                    # 방향 결정
                    if nr - cr == -1: next_dir = 1
                    elif nr - cr == 1: next_dir = 2
                    elif nc - cc == 1: next_dir = 4
                    else: next_dir = 3
                    
                    next_node = (nr, nc, dist + 1, next_dir)
                    candidates.append(next_node)
                    q.append((nr, nc, dist + 1, next_dir))
        
        # 정렬 기준: dist, row, col 순
        valid_candidates = [node for node in candidates if not visited[node[0]][node[1]]]
        if not valid_candidates:
            return None
        
        return min(valid_candidates, key=lambda x: (x[2], x[0], x[1]))

    # 시뮬레이션 루프
    for _ in range(N * N):
        if explore():
            print(f"{r + 1} {c + 1}")
            continue
        
        next_step = get_next_step()
        if not next_step:
            break
            
        r, c, _, d = next_step
        visited[r][c] = True
        print(f"{r + 1} {c + 1}")

solve()