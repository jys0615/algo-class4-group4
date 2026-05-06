"""
최소 스패닝 트리 - 크루스칼 알고리즘[파이썬 코드]
모든 노드를 연결하면서, 그 간선들의 가중치의 합이 최소인 부분 트리
대표적으로 크루스칼 알고리즘. 모든 정점을 최소한의 비용으로 연결하기 위한 상황에서 사용.
[수행 과정]
1. 간선 데이터를 비용에 따라 오름차순
2. 간선을 하나씩 확인하며 현재 간선이 사이클을 형성하는지 확인.
    사이클을 형성하지 않으면 최소 신장 트리에 포함.
    사이클을 형성하며 포함 안 한다.
3. 모든 간선에 대해 2. 과정을 반복한다.

최소 스패닝 트리도 트리 자료구조. 부분 트리에 포함되는 간선의 개수 = (노드의 개수 -1)
가장 짧은 간선부터 차례대로 집합에 추가한다. 단, 만약 추가되는 간선이 사이클 발생 시 
해당 간선은 제외한다. 
"""

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return x