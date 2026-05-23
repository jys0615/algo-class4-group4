import java.util.*;
import java.io.*;

class Node {
    int to;
    int cost;
    
    public Node(int to, int weight){
        this.to = to;
        this.cost = weight;
    }
}

class Solution {
    public static ArrayList<Node>[] graph;
    
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = Integer.MAX_VALUE;
        
        graph = new ArrayList [n+1];
        for(int i = 1; i < graph.length; i++){
            graph[i] = new ArrayList<>();
        }
        
        for(int i = 0; i < fares.length; i++){
            int start = fares[i][0];
            int end = fares[i][1];
            int weight = fares[i][2];
            
            graph[start].add(new Node(end, weight));
            graph[end].add(new Node(start, weight));
        }
        
        int[] together = dikjstra(s);
        for(int i = 1; i <= n; i++){
            int[] alone = dikjstra(i);
            answer = Math.min(answer, together[i] + alone[a] + alone[b]);
        }
        
        return answer;
    }
    
    public int[] dikjstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o1.cost - o2.cost);
        int[] dist = new int[graph.length];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;
        pq.add(new Node(start, 0));
        
        while(!pq.isEmpty()) {
            Node now = pq.poll();
            
            if(now.cost > dist[now.to])
                continue;
            
            for(int i = 0; i < graph[now.to].size(); i++){
                int newNode = graph[now.to].get(i).to;
                int newDist = dist[now.to] + graph[now.to].get(i).cost;
                
                if(newDist < dist[newNode]) {
                    pq.add(new Node(newNode, newDist));
                    dist[newNode] = newDist;
                }
            }
        }
        return dist;
    }
}