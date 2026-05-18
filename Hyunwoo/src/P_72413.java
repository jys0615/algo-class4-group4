package Lv3;

import java.util.*;

public class P_72413 {
    List<List<Node>> adj = new ArrayList<>();
    int[] sDist, aDist, bDist;

    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = Integer.MAX_VALUE;
        for (int i = 0; i <= n; i++)
            adj.add(new ArrayList<>());

        for (int[] fare : fares) {
            int start = fare[0];
            int end = fare[1];
            int weight = fare[2];
            adj.get(start).add(new Node(end, weight));
            adj.get(end).add(new Node(start, weight));
        }

        sDist = dijkstra(n, s);
        aDist = dijkstra(n, a);
        bDist = dijkstra(n, b);

        for (int i = 1; i <= n; i++)
            answer = Math.min(answer, sDist[i]+aDist[i]+bDist[i]);

        return answer;
    }

    int[] dijkstra(int n, int start) {
        int[] dist = new int[n+1];
        for (int i = 1; i <= n; i++)
            if (i != start)
                dist[i] = 100000 * n;

        Queue<Node> q = new PriorityQueue<>((o1, o2) -> {
            return o1.weight - o2.weight;
        });
        q.offer(new Node(start, 0));

        while(!q.isEmpty()) {
            Node currNode = q.poll();
            int curr = currNode.to;
            int weight = currNode.weight;
            if (dist[currNode.to] < currNode.weight)
                continue;

            for(Node nextNode : adj.get(currNode.to)) {
                int next = nextNode.to;
                int newWeight = dist[curr] + nextNode.weight;
                if (dist[next] > newWeight) {
                    dist[next] = newWeight;
                    q.offer(new Node(next, dist[next]));
                }
            }
        }

        return dist;
    }

    static class Node {
        int to, weight;
        Node (int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }

}
