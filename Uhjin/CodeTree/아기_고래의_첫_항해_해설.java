package Uhjin.CodeTree;

import java.util.Scanner;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Arrays;

public class 아기_고래의_첫_항해_해설 {
    static int N;
    static int[][] grid;
    static boolean[][] visited;

    // 반시계 방향: 상(0), 좌(1), 하(2), 우(3)
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, -1, 0, 1};

    // (r, c)가 격자 범위 내인지 확인합니다.
    static boolean inRange(int r, int c) {
        return 0 <= r && r < N && 0 <= c && c < N;
    }

    // (sr, sc)에서 출발하는 BFS를 수행하여
    // 모든 바다 칸까지의 최단 거리를 반환합니다.
    // 도달 불가능한 칸은 -1로 표시합니다.
    static int[][] bfs(int sr, int sc) {
        int[][] dist = new int[N][N];
        for (int[] row : dist) Arrays.fill(row, -1);
        dist[sr][sc] = 0;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{sr, sc});
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i], nc = c + dc[i];
                if (inRange(nr, nc) && grid[nr][nc] == 0 && dist[nr][nc] == -1) {
                    dist[nr][nc] = dist[r][c] + 1;
                    q.add(new int[]{nr, nc});
                }
            }
        }
        return dist;
    }

    // 1단계: 현재 위치와 방향에서 우선순위에 따라
    // 이동할 다음 칸을 반환합니다.
    // 이동 가능한 칸이 없으면 {-1, -1, -1}을 반환합니다.
    static int[] getNext(int r, int c, int d) {
        int[] deltas = {0, 1, -1, 2};
        for (int delta : deltas) {
            int nd = (d + delta + 4) % 4;
            int nr = r + dr[nd], nc = c + dc[nd];
            if (inRange(nr, nc) && grid[nr][nc] == 0 && !visited[nr][nc])
                return new int[]{nr, nc, nd};
        }
        return new int[]{-1, -1, -1};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        int r = sc.nextInt() - 1;
        int c = sc.nextInt() - 1;
        int d = sc.nextInt() - 1;

        // 입력 방향을 내부 표현으로 변환합니다.
        // 입력(0-indexed): 0=상, 1=하, 2=좌, 3=우
        // 내부(반시계):    0=상, 1=좌, 2=하, 3=우
        int[] dirMap = {0, 2, 1, 3};
        d = dirMap[d];

        grid = new int[N][N];
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                grid[i][j] = sc.nextInt();

        visited = new boolean[N][N];

        // 바다 칸의 총 개수를 셉니다.
        int total = 0;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                if (grid[i][j] == 0) total++;

        // 시작 위치를 방문 처리하고 출력합니다.
        visited[r][c] = true;
        System.out.println((r + 1) + " " + (c + 1));
        int cnt = 1;

        while (cnt < total) {
            // 1단계: 인접 탐험
            // 우선순위에 따라 이동 가능한 칸이 없을 때까지 반복합니다.
            while (true) {
                int[] next = getNext(r, c, d);
                if (next[0] == -1) break;
                r = next[0]; c = next[1]; d = next[2];
                visited[r][c] = true;
                cnt++;
                System.out.println((r + 1) + " " + (c + 1));
            }

            if (cnt >= total) break;

            // 2단계: 가장 가까운 미방문 바다 찾기
            // 현재 위치에서 BFS를 수행하여 거리맵을 구합니다.
            int[][] distFrom = bfs(r, c);

            // 미방문 바다 칸 중 최소 거리인 칸을 선택합니다.
            // 행-열 순서로 순회하므로 거리만 비교하면 됩니다.
            int tr = -1, tc = -1, minDist = -1;
            for (int i = 0; i < N; i++)
                for (int j = 0; j < N; j++) {
                    if (grid[i][j] != 0 || visited[i][j] || distFrom[i][j] == -1) continue;
                    if (minDist == -1 || distFrom[i][j] < minDist) {
                        tr = i; tc = j; minDist = distFrom[i][j];
                    }
                }

            // 목표 칸에서 BFS를 수행하여
            // 경로 추적에 필요한 거리맵을 구합니다.
            int[][] distTo = bfs(tr, tc);

            // 매 단계 목표까지의 거리가 1 줄어드는 방향 중
            // 좌, 하, 우, 상 순서로 우선순위가 높은 쪽을 선택합니다.
            int[] priority = {1, 2, 3, 0};
            while (r != tr || c != tc) {
                for (int dir : priority) {
                    int nr = r + dr[dir], nc = c + dc[dir];
                    if (inRange(nr, nc) && grid[nr][nc] == 0 && distTo[nr][nc] == distTo[r][c] - 1) {
                        r = nr; c = nc; d = dir;
                        break;
                    }
                }
            }

            // 목표 칸을 방문 처리하고 출력합니다.
            visited[r][c] = true;
            cnt++;
            System.out.println((r + 1) + " " + (c + 1));
        }
    }
}
