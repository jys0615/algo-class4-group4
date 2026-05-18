import heapq
def dijkstra(start, graph, n):
    INF = float('inf')
    dist = [INF] * (n+1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, v = heapq.heapop(heap)
        if cost > dist[v]:
            continue
        for nv, w in graph[v]:
            new_cost = cost + w
            if new_cost < dist[nv]:
                dist[nv] = new_cost
                heapq.heappush(heap, (new_cost, nv))

    return dist