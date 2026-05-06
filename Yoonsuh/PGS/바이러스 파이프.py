"""
1. 아이디어
- 파이프 타입 1,2,3 중 k번 이하 중복순열 백트래킹
- 각 순열마다 BFS로 감염 확산 시뮬레이션
- 감염된 노드 수 최대값 갱신

2. 시간복잡도
- 중복순열 : 3^k = 3^10 = 59049
- BFS : O(N) = 100
- 총합 : 59049 * 100 = 약 600만 > 가능

3. 자료구조
- 그래프 : 인접리스트 graph[]
- 감염 노드 : set
- Queue(BFS)
"""
from collections import deque
from itertools import product

def solution(n, infection, edges, k):
    graph = [[] for _ in range(n+1)]
    for x, y, t in edges:
        graph[x].append((y, t))
        graph[y].append((x, t))

    def bfs(infected, pipe_type):
        q = deque()
        new_infected = set(infected)
        for node in infected:
            for nxt, t in graph[node]:
                if t == pipe_type and nxt not in new_infected:
                    new_infected.add(nxt)
                    q.append(nxt)
        while q:
            node = q.popleft()
            for nxt, t in graph[node]:
                if t == pipe_type and nxt not in new_infected:
                    new_infected.add(nxt)
                    q.append(nxt)
        return new_infected

    maxv = 1
    # permutations X -> product (중복 허용)
    for r in range(1, k+1):
        for pipes in product([1, 2, 3], repeat=r):
            infected = {infection}
            for pipe_type in pipes:
                infected = bfs(infected, pipe_type)
            maxv = max(maxv, len(infected))

    return maxv