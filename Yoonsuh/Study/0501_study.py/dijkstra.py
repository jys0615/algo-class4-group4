"""
1. 아이디어
- 시작점에서 모든 노드까지 최단거리
- BFS + 우선순위 큐(heapq) 사용
- 꺼낼 때 이미 처리된 노드면 스킵

2. 시간복잡도
- O((V+E) log V)
- heapq push/pop : log V

3. 자료구조
- 그래프 : 인접리스트 graph[][]
- 거리 : int[] dist (INF 초기화)
- 우선순위 큐 : heapq
"""

import heapq
import sys
input = sys.stdin.readline

INF = float('inf')
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

def dijkstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    q = [(0, start)]
    while q:
        d, node = heapq.heappop(q)
        if dist[node] < d:
            continue
        for nxt, w in graph[node]:
            nd = dist[node] + w
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(q, (nd, nxt))
    return dist

rs = dijkstra(1)