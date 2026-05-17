import sys
input = sys.stdin.readline

### 기초 개념 및 암기 템플릿 ###
## 1. 이분 탐색 - 파라메트릭 서치 ##
"""
1. 아이디어
- "조건을 만족하는 최대/최솟값을 구하라" => 답 자체를 이분탐색
- check(mid) : mid가 조건을 만족하는지 확인
- 단조성 : check(k)가 참이면 check(k-1)도 참

2. 시간복잡도
- O(check 비용 * lgX) : X = 탐색 원리

3. 자료구조
- 탐색 범위 st, en : int
- 정답 후보 : rs
"""

st, en = 0, MAX
rs = -1

def check(mid):
    # mid 조건 만족 여부 반환
    pass

while st <= en:
    mid = (st + en) // 2
    if check(mid):
        rs = mid
        st = mid + 1 # 최대화 - 더 큰 값 탐색
        # end = mid - 1 # 최소화 - 더 작은 값 탐색
    else:
        en = mid -1

print(rs)

### 2차원 누적합 ###
"""
1. 아이디어
- 2D 격자에서 직사각형 구간합을 O(1)에 구하기
- prefix[i][j] = (0, 0 ~ (i-1, j-1) 직사각형 합
- 포함-배제 원리로 전처리 및 쿼리

2. 시간복잡도
- 전처리 : O(N*M)
- 쿼리 : O(1)

3. 자료구조
- 원본 격자 : int[][] (크기 N*M)
- 누적합 : int[][] prefix (크기 (N+1) * (M+1), 1-indexed)
"""

n, m = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]

# 전처리 - 반드시 암기
prefix = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j] = (map[i-1][j-1]+prefix[i-1][j]+prefix[i][j-1] - prefix[i-1][j-1])

def query(r1, c1, r2, c2):
    return (prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1])
