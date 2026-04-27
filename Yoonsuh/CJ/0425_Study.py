import sys
input = sys.stdin.readline

### 2.1 패턴 1: 시간복잡도 최적화 — 이분탐색/투포인터/누적합 ###
"""
1번은 해시나 정렬로 풀리는 경우가 많고, 2~3번은 브루트포스로 접근 시 시간 초과.
시간 복잡도를 개선하는 이분탐색/투포인터/슬라이딩 윈도우 중요
"""

## 이분 탐색 (매개변수 탐색) ## 
"""
조건을 만족하는 최소최대를 구하라. 정렬된 배열에서 특정값 위치
탐색 범위를 절반씩 줄여나가 O(logN)에 답을 찾는다. 
    암기법 - 파라메트릭 서치에서 lo = max(배열), hi = sum(배열)이 
    정석적 초기값이다.
"""

def parametric_search(lo, hi, is_possible):
    """
    is_possible(mid)가 참인 최소 찾기
    lo : 탐색 하한, hi: 탐색 상한
    """
    answer = hi + 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if is_possible(mid):
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return answer

def solve(arr, m):
    def can_split(max_sum):
        groups = 1
        curr = 0
        for x in arr:
            if curr + x > max_sum:
                groups += 1
                curr = x
            else:
                curr += x
        return groups <= m
    return parametric_search(max(arr), sum(arr), can_split)


def interval_dp(stones):
    """
    돌 합치기 (구간 DP)
    stones[i]: i번째 돌의 무게
    인접한 돌을 합칠 때 비용 = 두 돌의 무게 합
    모든 돌을 하나로 합치는 최소 비용
    """
    n = len(stones)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + stones[i]

    INF = float('inf')
    dp = [[INF] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            range_sum = prefix[j + 1] - prefix[i]
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + range_sum)

    return dp[0][n - 1]


from collections import Counter

arr = [1,2,2,3,3,3]
cnt = Counter(arr)

print(cnt) # Counter({3: 3, 2: 2, 1: 1})
print(cnt[3]) # 3->3이 몇개?
print(cnt.most_common(2)) ## 가장 많은 원소 2개 [(3, 3), (2, 2)]

s = "hello"
cnt = Counter(s) # {value:cnt}
print(cnt)
print(cnt['l'])

from collections import defaultdict

# 그룹핑 (키 없어도 에러 안 남)
d = defaultdict(list)
pairs = [("과일", "사과"), ("채소", "당근"), ("과일", "바나나")]

for category, item in pairs:
    d[category].append(item)

print(d["과일"])
print(d["음료"])

cnt = defaultdict(int)
for item in ["a", "b", "a", "c", "a"]:
    cnt[item]+=1

print(cnt["a"])
print(cnt["z"])

# 기본 정렬
arr = [3, 1, 4, 1, 5]
print(sorted(arr))              # 오름차순
print(sorted(arr, reverse=True)) # 내림차순

# 튜플 정렬 — 첫 번째 기준 오름차순
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
print(sorted(people, key=lambda x: x[1]))
# [('Bob', 25), ('Alice', 30), ('Charlie', 35)]

# 다중 조건 — 나이 오름차순, 같으면 이름 내림차순
print(sorted(people, key=lambda x: (x[1], x[0]), reverse=False))

# 음수 부호로 혼합 정렬 — 점수 내림차순, 이름 오름차순
scores = [("Alice", 90), ("Bob", 95), ("Charlie", 90)]
print(sorted(scores, key=lambda x: (-x[1], x[0])))
# [('Bob', 95), ('Alice', 90), ('Charlie', 90)]


# 테스트      
arr = [1, 2, 3, 4, 5]
M = 2
print(parametric_search(arr, M))  # 9