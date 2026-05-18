import heapq

def solution(n, s, a, b, fares):
    INF = float('inf')
    answer = INF
    taxi = [[] for _ in range(n+1)]
    
    for fare in fares:
        taxi[fare[0]].append((fare[1], fare[2]))
        taxi[fare[1]].append((fare[0], fare[2]))

        
    def dijkstra(start):
        distances = [INF] * (n + 1)
        distances[start] = 0
        queue = [(0, start)]

        while queue:
            curr_distance, curr_node = heapq.heappop(queue)

            if distances[curr_node] < curr_distance:
                continue

            for neighbor, weight in taxi[curr_node]:
                distance = curr_distance + weight
                # 새로 계산한 distance가 기존에 찾은 distance보다 작다면, distance 배열을 새로운 최소 비용으로 갱신한다.
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
        
        return distances

    # S, A, B 각 지점에서 출발하는 최단 거리 배열을 구한다.
    dist_from_s = dijkstra(s) # S -> i 비용
    dist_from_a = dijkstra(a) # i -> A 비용 (A -> i 비용과 같다)
    dist_from_b = dijkstra(b) # i -> B 비용 (B -> i 비용과 같다)

    # 모든 지점 i를 '합승이 끝나는 지점'으로 가정하고 최소 비용 계산한다.
    # 비용 = (S -> i 합승 비용) + (i -> A 비용) + (i -> B 비용)
    for i in range(1, n + 1):
        answer = min(answer, dist_from_s[i] + dist_from_a[i] + dist_from_b[i])

    return answer