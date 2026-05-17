"""
1. 아이디어
- DFS + 가지치기(pruning)
- 조건 불만족 시 즉시 되돌아옴
- 선택 -> 재귀 -> 취소 패턴

2. 시간복잡도
- 최악 O(N!) but 가지치기로 실제로는 훨씬 적음

3. 자료구조
- 체크 : bool[] chk
- 결과 : list rs
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
chk = [False] * (n+1)
rs = []

def dfs(depth):
    if depth == m:
        print(*rs)
        return
    for each in range(1, n+1):
        if not chk[each]:
            chk[each] = True
            rs.append(each)
            dfs(depth+1)
            rs.pop()
            chk[each] = False

dfs(0)