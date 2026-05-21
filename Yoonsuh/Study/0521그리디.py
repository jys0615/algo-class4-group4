# 1. 아이디어: 매 순간 최선의 선택 → 전체 최적
# 2. 시간복잡도: O(N log N) 정렬 + O(N) 순회
# 3. 자료구조: list, sorted()

import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    items = list(map(int, input().split()))

    # 그리디 기준으로 정렬
    items.sort()  # 또는 sort(key=lambda x: x[1]) 등

    rs = 0
    cur = 0  # 현재 상태 추적

    for each in items:
        # 그리디 선택 조건
        if 조건(each, cur):
            rs += 이득(each)
            cur = 갱신(each, cur)

    print(rs)

solve()