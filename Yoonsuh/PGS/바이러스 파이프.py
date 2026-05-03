from collections import deque
from itertools import permutations
def solution(n, infection, edges, k):
    graph = [[] for _ in range(n+1)]
    INF = float('inf')
    for item in edges:
        x, y, t = item
        graph[x].append((y, t))
        graph[y].append((x, t))
        
    def bfs(infected, pipe_type):
        q = deque()
        for node in infected:
            for nxt, t in graph[node]:
                if t == pipe_type and nxt not in infected:
                    q.append(nxt)
        new_infected = set(infected)
        while q:
            node = q.popleft()
            if node in new_infected:
                continue
            new_infected.add(node)
            for nxt, t in graph[node]:
                if t == pipe_type and nxt not in new_infected:
                    q.append(nxt)
        return new_infected
                
        
    maxv = 0
    
    for r in range(1, k+1):
        for pipes in permutations([1, 2, 3], r):
            infected = {infection}
            for pipe_type in pipes:
                infected = bfs(infected, pipe_type)
            maxv = max(maxv, len(infected))
            
        
            
    return maxv