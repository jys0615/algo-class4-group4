def solution(edges):
    
    def count_edges(edges):
        edge_counts = {}
        for a, b in edges:
            if not edge_counts.get(a):
                edge_counts[a] = [0,0]
            if not edge_counts.get(b):
                edge_counts[b] = [0,0]
                
            # 간선이 a에서 출발해 b로 들어가는 경우
            # [0] index에는 정점(a)에서 나가는 간선의 개수를 누적 계산
            # [1] index에서는 정점(b)으로 들어오는 간선의 개수를 누적 계산
            edge_counts[a][0] += 1
            edge_counts[b][1] += 1
            
        return edge_counts
    
    def check_answer(edge_counts):
        answer = [0,0,0,0]
        for key, counts in edge_counts.items():
            # 생성된 정점의 번호 확인
            # 생성된 정점은 기존 그래프들에 간선을 하나씩 새로 연결하므로 최소 2개 이상의 간선이 나가야 하고, 이 정점으로 들어오는 간선은 없어야 한다.
            if counts[0] >= 2 and counts[1] == 0:
                answer[0] = key
            # 막대 모양 그래프의 수 확인
            elif counts[0] == 0:
                answer[2] += 1
            # 8자 모양 그래프의 수 확인
            elif counts[0] >= 2 and counts[1] >= 2:
                answer[3] += 1
        
        # 도넛 모양 그래프의 수 확인
        # 전체 그래프 수 = 도넛 모양 그래프 수 + 막대 모양 그래프 수 + 8자 모양 그래프 수
        answer[1] = (edge_counts[answer[0]][0] - answer[2] - answer[3])
        
        return answer
    
    edge_counts = count_edges(edges)
    answer = check_answer(edge_counts)
    
    return answer