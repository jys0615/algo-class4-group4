def solution(m, n, h, w, drops):
    answer = []
    INF = float('inf')
    arr = [[INF]*n for _ in range(m)]
    for i, item in enumerate(drops):
        arr[item[0]][item[1]] = i + 1
        
    def check(mid):
        # 누적합을 담을 2차원 배열 - 인덱스 에러 방지 차원에서 크기 1씩 크게
        prefix = [[0] * (n+1) for _ in range(m + 1)]
        
        # arr 배열을 돌면서, mid 시간 이하에 떨어진 비면 1(젖음), 아니면 0(안전)으로 누적합 세팅.
        for i in range(m):
            for j in range(n):
                is_wet = 1 if arr[i][j] <= mid else 0
                prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + is_wet
        
        for i in range(m - h + 1):
            for j in range(n - w + 1):
                r1, c1 = i, j
                r2, c2 = i + h - 1, j + w - 1
                
                # 누적합을 이용해 (r1, c1)부터 (r2, c2)까지의 젖은 칸 개수를 O(1)로 계산
                # prefix는 1-Indexed므로 r2, c2 쪽에 +1을 한다.
                wet_count = (prefix[r2+1][c2+1] - prefix[r1][c2+1]
                            - prefix[r2+1][c1] + prefix[r1][c1])
                
                if wet_count == 0:
                    return [r1, c1]
        return None
        
    low = 0
    high = len(drops)
    
    ans = [0, 0]
    
    while low <= high:
        mid = (low + high) // 2
        
        result = check(mid)
        
        if result:
            ans = result
            low = mid + 1
        else:
            high = mid - 1
            
    return ans           

"""
[오답 코드]
>> 테케 6개는 정답이나, 시간복잡도 초과 발생.
>> 이유는 뻔한 게,,,,4중 for문!!!!!!!
def solution(m, n, h, w, drops):
    answer = []
    INF = float('inf')
    arr = [[INF]*n for _ in range(m)]
    for i, item in enumerate(drops):
        arr[item[0]][item[1]] = i + 1
    
    minv = float('inf')
    for i in range(m - h + 1):
        for j in range(n - w + 1):
            r1, c1 = i, j
            r2, c2 = i + h - 1, j + w -1
            load = []
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    if load:
                        if minv > arr[r][c]:
                            load.pop()
                            minv = arr[r][c]
                            load.append((arr[r][c], r1, c1))
                    else:
                        minv = arr[r][c]
                        load.append((arr[r][c], r1, c1))
            answer.append(load.pop())
    maxv = 0
    ans = 0, 0
    for val, i, j in answer:
        if maxv < val:
            maxv = val
            ans = i, j
            
    return ans     
"""