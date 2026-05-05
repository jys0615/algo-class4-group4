from collections import deque

def solution(m, n, h, w, drops):
    answer = []
    # 끝까지 비가 오지 않는 칸의 시간
    INF = len(drops) + 1
    
    # 각 칸이 몇 번째로 비를 맞는지 순서를 기록한다.
    time = [[INF] * n for _ in range(m)]
    for i in range(len(drops)):
        a, b = drops[i]
        time[a][b] = i + 1  
        
        
    width = n - w + 1
    row_min = [[0] * width for _ in range(m)]
    
    for i in range(m):
        # d에 최솟값 인덱스를 넣어준다.
        d = deque()
        for j in range(n):
            # 새로 들어오는 값보다 기존 deque 내 값들이 더 큰 경우, 해당 값들은 앞으로도 최솟값이 될 수 없으므로 pop해서 제거한다. 
            while d and time[i][d[-1]] >= time[i][j]:
                d.pop()
            d.append(j)            
            # 현재 격자 범위를 벗어난 인덱스 제거
            while d and d[0] <= j - w:
                d.popleft()
            # 범위가 다 차는 순간(인덱스가 w-1 되는 순간) 이후부터 deque의 맨 앞 최솟값을 결과에 기록
            if j >= w - 1:
                row_min[i][j - w + 1] = time[i][d[0]]
                
                
    height = m - h + 1
    rect_min = [[0] * width for _ in range(height)]
    
    # 행 방향이 아니라 열 방향으로도 같은 작업을 반복한다.
    for j in range(width):
        d = deque()
        for i in range(m):
            while d and row_min[d[-1]][j] >= row_min[i][j]:
                d.pop()
            d.append(i)            
            while d and d[0] <= i - h:
                d.popleft()
            if i >= h - 1:
                rect_min[i - h + 1][j] = row_min[d[0]][j]      
    
    
    # 선인장 구역에 대하여 가장 먼저 비를 맞는 시간(최솟값)을 다 구했으므로 이 중에서 가장 늦은 시간(최댓값)을 구하면 된다.
    maximum = -1
    answer = [0, 0]
    
    for i in range(height):
        for j in range(width):
            if rect_min[i][j] > maximum:
                # 가장 늦게 비를 맞는 시간(최댓값)을 계속 업데이트하고, 그때의 왼쪽 위칸의 좌표를 answer에 저장한다. 
                maximum = rect_min[i][j]
                answer = [i, j]
    
    
    return answer